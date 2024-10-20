![Fast Data Science logo](https://raw.githubusercontent.com/fastdatascience/brand/main/primary_logo.svg)

<a href="https://fastdatascience.com"><span align="left">🌐 fastdatascience.com</span></a>
<a href="https://www.linkedin.com/company/fastdatascience/"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/linkedin.svg" alt="Fast Data Science | LinkedIn" width="21px"/></a>
<a href="https://twitter.com/fastdatascienc1"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/x.svg" alt="Fast Data Science | X" width="21px"/></a>
<a href="https://www.instagram.com/fastdatascience/"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/instagram.svg" alt="Fast Data Science | Instagram" width="21px"/></a>
<a href="https://www.facebook.com/fastdatascienceltd"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/fb.svg" alt="Fast Data Science | Facebook" width="21px"/></a>
<a href="https://www.youtube.com/channel/UCLPrDH7SoRT55F6i50xMg5g"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/yt.svg" alt="Fast Data Science | YouTube" width="21px"/></a>
<a href="https://g.page/fast-data-science"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/google.svg" alt="Fast Data Science | Google" width="21px"/></a>
<a href="https://medium.com/fast-data-science"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/medium.svg" alt="Fast Data Science | Medium" width="21px"/></a>
<a href="https://mastodon.social/@fastdatascience"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/mastodon.svg" alt="Fast Data Science | Mastodon" width="21px"/></a>

# Medical Named Entity Recognition Python library by Fast Data Science

## Finds disease names

<!-- badges: start -->
![my badge](https://badgen.net/badge/Status/In%20Development/orange)
[![PyPI package](https://img.shields.io/badge/pip%20install-medical_named_entity_recognition-brightgreen)](https://pypi.org/project/medical-named-entity-recognition/) [![version number](https://img.shields.io/pypi/v/medical-named-entity-recognition?color=green&label=version)](https://github.com/fastdatascience/medical_named_entity_recognition/releases) [![License](https://img.shields.io/github/license/fastdatascience/medical_named_entity_recognition)](https://github.com/fastdatascience/medical_named_entity_recognition/blob/main/LICENSE)
[![pypi Version](https://img.shields.io/pypi/v/medical_named_entity_recognition.svg?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/medical_named_entity_recognition/)
 [![version number](https://img.shields.io/pypi/v/medical_named_entity_recognition?color=green&label=version)](https://github.com/fastdatascience/medical_named_entity_recognition/releases) [![PyPi downloads](https://static.pepy.tech/personalized-badge/medical_named_entity_recognition?period=total&units=international_system&left_color=grey&right_color=orange&left_text=pip%20downloads)](https://pypi.org/project/medical_named_entity_recognition/)
[![forks](https://img.shields.io/github/forks/fastdatascience/medical_named_entity_recognition)](https://github.com/fastdatascience/medical_named_entity_recognition/forks)

<!-- badges: end -->

# ⚕️ Medical Named Entity Recognition

Developed by Fast Data Science, https://fastdatascience.com

Source code at https://github.com/fastdatascience/medical_named_entity_recognition

This library is in Beta.

## 😊 Who worked on the Medical Named Entity Recognition library?

The tool was developed by:

* Thomas Wood ([Fast Data Science](https://fastdatascience.com))

# 💻Installing Medical Named Entity Recognition Python package

You can install Medical Named Entity Recognition from [PyPI](https://pypi.org/project/drug-named-entity-recognition).

```
pip install medical-named-entity-recognition
```

If you get an error installing Medical Named Entity Recognition, try making a new Python environment in Conda (`conda create -n test-env; conda activate test-env`) or Venv (`python -m testenv; source testenv/bin/activate` / `testenv\Scripts\activate`) and then installing the library.

# 💡Usage examples

You must first tokenise your input text using a tokeniser of your choice (NLTK, spaCy, etc).

You pass a list of strings to the `find_diseases` function.

Example 1

```
import re
re_tokenise = re.compile(r"((?:\w|'|’)+)")
from medical_named_entity_recognition import find_diseases
tokens = re_tokenise.findall("cystic fibrosis")
find_diseases(tokens)
```

outputs a list of tuples.

```
[({'mesh_id': 'D019005',
   'mesh_tree': ['C16.320.190', 'C16.614.213', 'C08.381.187', 'C06.689.202'],
   'name': 'Cystic Fibrosis',
   'synonyms': ['cystic fibrosis',
    'mucoviscidosis',
    'pancreas fibrocystic diseases',
    'pancreas fibrocystic disease',
    'cystic fibrosis, pulmonary',
    'cystic fibrosis, pancreatic',
    'pancreatic cystic fibrosis',
    'fibrosis, cystic',
    'pulmonary cystic fibrosis',
    'fibrocystic disease of pancreas',
    'cystic fibrosis of pancreas'],
   'is_brand': False,
   'match_type': 'exact',
   'matching_string': 'cystic fibrosis'},
  0,
  1)]
```


# Interested in other kinds of named entity recognition (NER)? 💊 Drug names (medicines), pharma, 💸Finances, 🎩company names, 🌎countries, 🗺️locations, proteins, 🧬genes, 🧪molecules?

If your NER problem is common across industries and likely to have been seen before, there may be an off-the-shelf NER tool for your purposes, such as our [Country Named Entity Recognition](https://fastdatascience.com/natural-language-processing/country-named-entity-recognition/) Python library or our [Drug Named Entity Recognition](https://fastdatascience.com/ai-in-pharma/drug-named-entity-recognition-python-library/) library. Dictionary-based named entity recognition is not always the solution, as sometimes the total set of entities is an open set and can't be listed (e.g. personal names), so sometimes a bespoke trained NER model is the answer. For tasks like finding email addresses or phone numbers, regular expressions (simple rules) are sufficient for the job.

If your named entity recognition or named entity linking problem is very niche and unusual, and a product exists for that problem, that product is likely to only solve your problem 80% of the way, and you will have more work trying to fix the final mile than if you had done the whole thing manually. Please [contact Fast Data Science](http://fastdatascience.com/contact) and we'll be glad to discuss. For example, we've worked on [a consultancy engagement to find molecule names in papers, and match author names to customers](https://fastdatascience.com/ai-in-pharma/finding-molecules-and-proteins-in-scientific-literature/) where the goal was to trace molecule samples ordered from a pharma company and identify when the samples resulted in a publication. For this case, there was no off-the-shelf library that we could use.

For a problem like identifying country names in English, which is a closed set with well-known variants and aliases, an off-the-shelf library is usually available. You may wish to try our [Country Named Entity Recognition](https://fastdatascience.com/natural-language-processing/country-named-entity-recognition/) library, also open-source and under MIT license.

For identifying a set of molecules manufactured by a particular company, this is the kind of task more suited to a [consulting engagement](https://fastdatascience.com/natural-language-processing/nlp-consultant/).


# Requirements

Python 3.9 and above

## ✉️Who to contact?

You can contact Thomas Wood or the Fast Data Science team at https://fastdatascience.com/.


## Contributing to the Medical Named Entity Recognition library

If you'd like to contribute to this project, you can contact us at https://fastdatascience.com/ or make a pull request on our [Github repository](https://github.com/fastdatascience/medical_named_entity_recognition). You can also [raise an issue](https://github.com/fastdatascience/medical_named_entity_recognition/issues). 

## Developing the Medical Named Entity Recognition library

### Automated tests

Test code is in **tests/** folder using [unittest](https://docs.python.org/3/library/unittest.html).

The testing tool `tox` is used in the automation with GitHub Actions CI/CD.

### Use tox locally

Install tox and run it:

```
pip install tox
tox
```

In our configuration, tox runs a check of source distribution using [check-manifest](https://pypi.org/project/check-manifest/) (which requires your repo to be git-initialized (`git init`) and added (`git add .`) at least), setuptools's check, and unit tests using pytest. You don't need to install check-manifest and pytest though, tox will install them in a separate environment.

The automated tests are run against several Python versions, but on your machine, you might be using only one version of Python, if that is Python 3.9, then run:

```
tox -e py39
```

Thanks to GitHub Actions' automated process, you don't need to generate distribution files locally. But if you insist, click to read the "Generate distribution files" section.

### 🤖 Continuous integration/deployment to PyPI

This package is based on the template https://pypi.org/project/example-pypi-package/

This package

- uses GitHub Actions for both testing and publishing
- is tested when pushing `master` or `main` branch, and is published when create a release
- includes test files in the source distribution
- uses **setup.cfg** for [version single-sourcing](https://packaging.python.org/guides/single-sourcing-package-version/) (setuptools 46.4.0+)

## 🧍Re-releasing the package manually

The code to re-release Medical Named Entity Recognition on PyPI is as follows:

```
source activate py311
pip install twine
rm -rf dist
python setup.py sdist
twine upload dist/*
```

## 😊 Who worked on the Medical Named Entity Recognition library?

The tool was developed by:

* Thomas Wood ([Fast Data Science](https://fastdatascience.com))

# 🤝Compatibility with other natural language processing libraries

The Medical Named Entity Recognition library is independent of other NLP tools and has no dependencies. You don't need any advanced system requirements and the tool is lightweight. However, it combines well with other libraries  such as [spaCy](https://spacy.io) or the [Natural Language Toolkit (NLTK)](https://www.nltk.org/api/nltk.tokenize.html).

## 📜License of Medical Named Entity Recognition library

MIT License. Copyright (c) 2024 [Fast Data Science](https://fastdatascience.com)
