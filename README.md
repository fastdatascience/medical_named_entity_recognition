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

# 💊 Medical Named Entity Recognition

Developed by Fast Data Science, https://fastdatascience.com

Source code at https://github.com/fastdatascience/medical_named_entity_recognition

This library is in Beta.

## 😊 Who worked on the Medical Named Entity Recognition library?

The tool was developed by:

* Thomas Wood ([Fast Data Science](https://fastdatascience.com))

# 💻Installing Drug Named Entity Recognition Python package

You can install Drug Named Entity Recognition from [PyPI](https://pypi.org/project/drug-named-entity-recognition).

```
pip install medical-named-entity-recognition
```

If you get an error installing Medical Named Entity Recognition, try making a new Python environment in Conda (`conda create -n test-env; conda activate test-env`) or Venv (`python -m testenv; source testenv/bin/activate` / `testenv\Scripts\activate`) and then installing the library.

# 💡Usage examples

You must first tokenise your input text using a tokeniser of your choice (NLTK, spaCy, etc).

You pass a list of strings to the `find_diseases` function.

Example 1

```
from drug_named_entity_recognition import find_diseases
tokens = re_tokenise.findall("cystic fibrosis")
find_diseases(tokens, is_ignore_case=True)
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


## 📜License of Medical Named Entity Recognition library

MIT License. Copyright (c) 2024 [Fast Data Science](https://fastdatascience.com)
