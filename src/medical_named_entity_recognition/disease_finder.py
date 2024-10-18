'''
MIT License

Copyright (c) 2023 Fast Data Science Ltd (https://fastdatascience.com)

Maintainer: Thomas Wood

Tutorial at https://fastdatascience.com/drug-named-entity-recognition-python-library/

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

import bz2
import pathlib
import pickle as pkl
import re
from collections import Counter

re_apostrophe = re.compile(r"'|’")

from medical_named_entity_recognition.util import stopwords

this_path = pathlib.Path(__file__).parent.resolve()

with bz2.open(this_path.joinpath("disease_ner_dictionary.pkl.bz2"), "rb") as f:
    d = pkl.load(f)

disease_variant_to_canonical = {}
disease_canonical_to_data = {}
disease_variant_to_variant_data = {}
ngram_to_variant = {}
variant_to_ngrams = {}


def get_ngrams(text):
    n = 3
    ngrams = set()
    for i in range(0, len(text) - n + 1, 1):
        ngrams.add(text[i:i + n])
    return ngrams


# Load dictionary from disk
def reset_diseases_data():
    disease_variant_to_canonical.clear()
    disease_canonical_to_data.clear()
    disease_variant_to_variant_data.clear()
    ngram_to_variant.clear()
    variant_to_ngrams.clear()

    disease_variant_to_canonical.update(d["disease_variant_to_canonical"])
    disease_canonical_to_data.update(d["disease_canonical_to_data"])
    disease_variant_to_variant_data.update(d["disease_variant_to_variant_data"])

    for variant, canonicals in disease_variant_to_canonical.items():
        for canonical in canonicals:
            if canonical in disease_canonical_to_data:
                if "synonyms" not in disease_canonical_to_data[canonical]:
                    disease_canonical_to_data[canonical]["synonyms"] = []
                disease_canonical_to_data[canonical]["synonyms"].append(variant)

    for disease_variant in disease_variant_to_canonical:
        ngrams = get_ngrams(disease_variant)
        variant_to_ngrams[disease_variant] = ngrams
        for ngram in ngrams:
            if ngram not in ngram_to_variant:
                ngram_to_variant[ngram] = []
            ngram_to_variant[ngram].append(disease_variant)


def add_custom_disease_synonym(disease_variant: str, canonical_name: str, optional_variant_data: dict = None):
    disease_variant = disease_variant.lower()
    canonical_name = canonical_name.lower()
    disease_variant_to_canonical[disease_variant] = [canonical_name]
    if optional_variant_data is not None and len(optional_variant_data) > 0:
        disease_variant_to_variant_data[disease_variant] = optional_variant_data

    ngrams = get_ngrams(disease_variant)
    variant_to_ngrams[disease_variant] = ngrams
    for ngram in ngrams:
        if ngram not in ngram_to_variant:
            ngram_to_variant[ngram] = []
        ngram_to_variant[ngram].append(disease_variant)

    return f"Added {disease_variant} as a synonym for {canonical_name}. Optional data attached to this synonym = {optional_variant_data}"


def add_custom_new_disease(disease_name, disease_data):
    disease_name = disease_name.lower()
    disease_canonical_to_data[disease_name] = disease_data
    add_custom_disease_synonym(disease_name, disease_name)

    return f"Added {disease_name} to the tool with data {disease_data}"


def remove_disease_synonym(disease_variant: str):
    disease_variant = disease_variant.lower()
    ngrams = get_ngrams(disease_variant)

    del variant_to_ngrams[disease_variant]
    del disease_variant_to_canonical[disease_variant]
    del disease_variant_to_variant_data[disease_variant]

    for ngram in ngrams:
        ngram_to_variant[ngram].remove(disease_variant)

    return f"Removed {disease_variant} from dictionary"


def get_fuzzy_match(surface_form: str):
    query_ngrams = get_ngrams(surface_form)
    candidate_to_num_matching_ngrams = Counter()
    for ngram in query_ngrams:
        candidates = ngram_to_variant.get(ngram, None)
        if candidates is not None:
            for candidate in candidates:
                candidate_to_num_matching_ngrams[candidate] += 1

    candidate_to_jaccard = {}
    for candidate, num_matching_ngrams in candidate_to_num_matching_ngrams.items():
        ngrams_in_query_and_candidate = query_ngrams.union(variant_to_ngrams[candidate])
        jaccard = num_matching_ngrams / len(ngrams_in_query_and_candidate)
        candidate_to_jaccard[candidate] = jaccard

    query_length = len(surface_form)
    if len(candidate_to_num_matching_ngrams) > 0:
        top_candidate = max(candidate_to_jaccard, key=candidate_to_jaccard.get)
        jaccard = candidate_to_jaccard[top_candidate]
        query_ngrams_missing_in_candidate = query_ngrams.difference(variant_to_ngrams[top_candidate])
        candidate_ngrams_missing_in_query = variant_to_ngrams[top_candidate].difference(query_ngrams)

        candidate_length = len(top_candidate)
        length_diff = abs(query_length - candidate_length)
        if max([len(query_ngrams_missing_in_candidate), len(candidate_ngrams_missing_in_query)]) <= 3 \
                and length_diff <= 2:
            return top_candidate, jaccard
    return None, None


def find_diseases(tokens: list, is_fuzzy_match=False, is_ignore_case=None):
    """

    @param tokens:
    @param is_fuzzy_match:
    @param is_ignore_case: just for backward compatibility
    @return:
    """

    disease_matches = []
    is_exclude = set()

    # Search for 2 token sequences
    for token_idx, token in enumerate(tokens[:-1]):
        next_token = tokens[token_idx + 1]
        cand = token + " " + next_token
        cand_norm = cand.lower()

        match = disease_variant_to_canonical.get(cand_norm, None)
        if match is None:
            cand_norm_2 = re_apostrophe.sub("", cand_norm)
            disease_variant_to_canonical.get(cand_norm_2, None)

        if match:

            for m in match:
                match_data = dict(disease_canonical_to_data.get(m, {})) | disease_variant_to_variant_data.get(cand_norm,
                                                                                                              {})
                match_data["match_type"] = "exact"
                match_data["matching_string"] = cand

                disease_matches.append((match_data, token_idx, token_idx + 1))
                is_exclude.add(token_idx)
                is_exclude.add(token_idx + 1)
        elif is_fuzzy_match:
            if token.lower() not in stopwords and next_token.lower() not in stopwords:
                fuzzy_matched_variant, similarity = get_fuzzy_match(cand_norm)
                if fuzzy_matched_variant is not None:
                    match = disease_variant_to_canonical[fuzzy_matched_variant]
                    for m in match:
                        match_data = dict(disease_canonical_to_data.get(m, {})) | disease_variant_to_variant_data.get(
                            fuzzy_matched_variant, {})
                        match_data["match_type"] = "fuzzy"
                        match_data["match_similarity"] = similarity
                        match_data["match_variant"] = fuzzy_matched_variant
                        match_data["matching_string"] = cand
                        disease_matches.append((match_data, token_idx, token_idx + 1))

    for token_idx, token in enumerate(tokens):
        if token_idx in is_exclude:
            continue
        cand_norm = token.lower()
        match = disease_variant_to_canonical.get(cand_norm, None)
        if match is None:
            cand_norm_2 = re_apostrophe.sub("", cand_norm)
            disease_variant_to_canonical.get(cand_norm_2, None)

        if match:
            for m in match:
                match_data = dict(disease_canonical_to_data.get(m, {})) | disease_variant_to_variant_data.get(cand_norm,
                                                                                                              {})
                match_data["match_type"] = "exact"
                match_data["matching_string"] = token
                disease_matches.append((match_data, token_idx, token_idx))
        elif is_fuzzy_match:
            if cand_norm not in stopwords and len(cand_norm) > 3:
                fuzzy_matched_variant, similarity = get_fuzzy_match(cand_norm)
                if fuzzy_matched_variant is not None:
                    match = disease_variant_to_canonical[fuzzy_matched_variant]
                    for m in match:
                        match_data = dict(disease_canonical_to_data.get(m, {})) | disease_variant_to_variant_data.get(
                            fuzzy_matched_variant, {})
                        match_data["match_type"] = "fuzzy"
                        match_data["match_similarity"] = similarity
                        match_data["match_variant"] = fuzzy_matched_variant
                        match_data["matching_string"] = token
                        disease_matches.append((match_data, token_idx, token_idx + 1))

    return disease_matches


reset_diseases_data()

print(find_diseases("cystic fibrosis".split()))
