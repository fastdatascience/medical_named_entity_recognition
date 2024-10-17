'''
MIT License

Copyright (c) 2023 Fast Data Science Ltd (https://fastdatascience.com)

Maintainer: Thomas Wood

Tutorial at https://fastdatascience.com/disease-named-entity-recognition-python-library/

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
import csv
import json
import pathlib
import pickle as pkl
import re

from nltk.corpus import words

re_num = re.compile(r'^\d+$')
re_three_digits = re.compile(r'\d\d\d')

this_path = pathlib.Path(__file__).parent.resolve()

disease_variant_to_canonical = {}
disease_canonical_to_data = {}
disease_variant_to_variant_data = {}


def add_canonical(canonical: str, data: dict):
    canonical_norm = canonical.lower().strip()
    if canonical_norm in disease_variant_to_canonical and canonical_norm not in disease_variant_to_canonical[canonical_norm]:
        print(f"Adding canonical {canonical_norm} but it already maps to {disease_variant_to_canonical[canonical_norm]}")
        canonical_norm = disease_variant_to_canonical[canonical_norm][0]
    elif canonical_norm not in disease_variant_to_canonical:
        data["name"] = canonical
    if canonical_norm not in disease_canonical_to_data:
        disease_canonical_to_data[canonical_norm] = data
    else:
        disease_canonical_to_data[canonical_norm] = disease_canonical_to_data[canonical_norm] | data


def add_synonym(synonym: str, canonical: str, synonym_data: dict = None):
    canonical_norm = canonical.lower().strip()
    synonym_norm = synonym.lower().strip()
    if synonym_norm not in disease_variant_to_canonical:
        disease_variant_to_canonical[synonym_norm] = [canonical_norm]
    else:
        if canonical_norm not in disease_variant_to_canonical:
            disease_variant_to_canonical[synonym_norm].append(canonical_norm)
    if synonym_data is not None:
        if synonym_norm not in disease_variant_to_variant_data:
            disease_variant_to_variant_data[synonym_norm] = synonym_data
        else:
            disease_variant_to_variant_data[synonym_norm] = disease_variant_to_variant_data[synonym_norm] | synonym_data



with open(this_path.joinpath("diseases_dictionary_mesh.csv"), 'r', encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    headers = None
    for row in csv_reader:
        if not headers:
            headers = row
            continue
        id = row[0]
        generic_names = row[1].split("|")
        common_name = row[2]
        synonyms = row[3].split("|")
        tree = row[4].split("|")
        data = {"mesh_id": id, "mesh_tree": tree}

        canonical = common_name
        add_canonical(canonical, data)
        for synonym in generic_names:
            add_synonym(synonym, canonical, {"is_brand": False})
        add_synonym(common_name, canonical)
        for synonym in synonyms:
            add_synonym(synonym, canonical)


# Remove common English words

print("Finding all diseases that are also in the NLTK list of English words.")

from nltk.corpus import stopwords

stops = set(stopwords.words('english'))

all_english_vocab = set([w.lower() for w in words.words()])

words_to_check_with_ai = set()
for word in list(disease_variant_to_canonical):
    reason = None
    if word in stops:
        reason = "it is an English word in stopword list"
    # elif len(word) < 4:
    #     reason = "it is short"
    # elif len(re_num.findall(word)) > 0:
    #     reason = "it is numeric"
    # elif len(word) > 50:
    #     reason = "it is too long"
    # elif "(" in word or "//" in word:
    #     reason = "it contains forbidden punctuation"
    # elif len(re_three_digits.findall(word)) > 0:
    #     reason = "it contains 3 or more consecutive digits"
    if reason is not None:
        print(f"Removing [{word}] from disease dictionary because {reason}")
        del disease_variant_to_canonical[word]

canonical_has_variants_pointing_to_it = set()
for variant, canonicals in disease_variant_to_canonical.items():
    for canonical in canonicals:
        canonical_has_variants_pointing_to_it.add(canonical)

with open("words_to_check_with_ai.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(words_to_check_with_ai))

# Find any redirects that go through twice

all_redirects_fixed = set()
for i in range(3):
    print(f"Normalising redirects step {i}")
    redirects_needed = {}
    for variant, canonicals in list(disease_variant_to_canonical.items()):
        for canonical in canonicals:
            if canonical in disease_variant_to_canonical:
                for canonical_of_canonical in disease_variant_to_canonical[canonical]:
                    if canonical_of_canonical != canonical:
                        redirects_needed[variant] = disease_variant_to_canonical[canonical]
                        all_redirects_fixed.add(variant)
    print(f"There are {len(redirects_needed)} disease names which are redirected twice. These need to be normalised")
    for source, targets in redirects_needed.items():
        disease_variant_to_canonical[source] = targets

for variant in all_redirects_fixed:
    canonicals = disease_variant_to_canonical[variant]
    for canonical in canonicals:
        synonyms = set(disease_canonical_to_data[canonical].get("synonyms", []))
        if variant not in synonyms:
            print(f"Variant {variant} not listed as synonym of {canonical}. Adding it")
            synonyms.add(variant)
            disease_canonical_to_data[canonical]["synonyms"] = sorted(synonyms)

# Remove any entries in the database that will never be used because nothing points there

for canonical in list(disease_canonical_to_data):
    if canonical not in canonical_has_variants_pointing_to_it:
        print(f"removing data for {canonical} because there are no synonyms pointing to it")
        del disease_canonical_to_data[canonical]

with bz2.open("../src/medical_named_entity_recognition/disease_ner_dictionary.pkl.bz2", "wb") as f:
    pkl.dump(
        {"disease_variant_to_canonical": disease_variant_to_canonical,
         "disease_canonical_to_data": disease_canonical_to_data,
         "disease_variant_to_variant_data": disease_variant_to_variant_data},
        f
    )
