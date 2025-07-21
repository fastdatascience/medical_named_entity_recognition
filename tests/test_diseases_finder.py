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

import unittest

from medical_named_entity_recognition.disease_finder import find_diseases


class TestDiseaseFinder(unittest.TestCase):

    def test_diseases_no_overlap(self):
        diseases = find_diseases("cystic fibrosis".split(" "), is_allow_overlapping_disease_names=False)

        self.assertEqual(1, len(diseases))
        self.assertEqual("Cystic Fibrosis", diseases[0][0]['name'])

    def test_diseases_allow_overlap(self):
        diseases = find_diseases("cystic fibrosis".split(" "))

        self.assertEqual(2, len(diseases))
        self.assertEqual("Cystic Fibrosis", diseases[0][0]['name'])

    def test_neuroendocrine(self):
        diseases = find_diseases("Neuroendocrine Neoplasms".split(" "))

        self.assertEqual(2, len(diseases))
        self.assertEqual("Neuroendocrine Tumors", diseases[0][0]['name'])
