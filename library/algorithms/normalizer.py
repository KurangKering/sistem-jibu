from library.algorithms.damerau import DamerauLevenshtein
from library.algorithms import dictionary
from library.algorithms.ngram import BasicNGram
from library.algorithms.probability import BasicProbability
from library.algorithms.scoring import BasicScoring
from copy import deepcopy


class DamerauNormalizer:

    def __init__(self, dictionary):

        levenshtein = DamerauLevenshtein()

        self._normalizer = ImplementDamerauNormalisasi(dictionary.as_dict(), levenshtein)

    def normalisasi(self, words):
        output = self._normalizer.normalisasi(words)
        return output

class ImplementDamerauNormalisasi:
    _sentence = ""
    _output = ""

    _dictionary_alg = None
    _levenshtein_alg = None

    def __init__(self, dictionary, levenshtein):
        self._dictionary_alg = dictionary
        self._levenshtein_alg = levenshtein

    def normalisasi(self, words):
        self._set_sentence(words)

        levenshtein = self._create_levenshtein(self._dictionary_alg, self._sentence)

        self._set_C_number(levenshtein)
        self._set_C(levenshtein)

        return self

    def _create_levenshtein(self, dictionary, sentence):
        levenshtein = self._levenshtein_alg.execute(dictionary, sentence)
        return levenshtein

    def _set_sentence(self, sentence):
        sentence = " ".join(sentence.split())
        self._sentence = sentence

    def _set_C(self, raw_C):
        self._C =  [list(x.keys()) for x in raw_C]

    def _set_C_number(self, raw_C):
        self._C_number = deepcopy(raw_C)

    def get_sentence(self):
        return self._sentence

    def get_C(self):
        return self._C

    def get_C_number(self):
        return self._C_number

    def get_output_str(self):
        return " ".join(self._output)

    
