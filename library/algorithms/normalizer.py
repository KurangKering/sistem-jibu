from library.algorithms.damerau import DamerauLevenshtein
from library.algorithms import dictionary
from library.algorithms.ngram import BasicNGram
from library.algorithms.probability import BasicProbability
from library.algorithms.scoring import BasicScoring
from copy import deepcopy



class BasicNormalizer:

    def __init__(self, dictionary):
        self._normalizer = ImplementBasicNormalisasi(dictionary)

    def normalisasi(self, words):
        output = self._normalizer.normalisasi(words)
        return output

class ImplementBasicNormalisasi:
    _C = []
    _C_number = []
    _W = []
    _sentence = ""
    _score = []
    _probability = []
    _grams = []
    _freqs = []
    _output = ""
    
    _dictionary_alg = None
    _ngram_alg = None
    _damerau_alg = None
    _probability_alg = None
    _scoring_alg = None
    
    def __init__(self, dictionary):
        self._dictionary_alg = dictionary
        self._damerau_alg = DamerauLevenshtein()
        self._ngram_alg = BasicNGram()
        self._probability_alg = BasicProbability()
        self._scoring_alg = BasicScoring()
    
    def normalisasi(self, words):
        self._set_sentence(words)
        self._set_W(self._sentence)
        
        damerau = self._damerau_alg.execute(self._dictionary_alg, self._sentence)
        self._set_C_number(damerau)
        self._set_C(damerau)

        self._grams, self._freqs = self._ngram_alg.execute(self._C, self._W)
        self._probability =  self._probability_alg.execute(self._C, (self._grams, self._freqs))
        self._score, self._output = self._scoring_alg.execute(self._C, self._probability)
        
        return self
    
    def _set_C(self, raw_C):
        self._C =  [list(x.keys()) for x in raw_C]

    def _set_C_number(self, raw_C):
        self._C_number = deepcopy(raw_C)
        
    def _set_W(self, sentence):
        token = sentence.split()
        self._W = deepcopy(token)
        self._W.insert(0,'_')
        self._W.insert(len(token)+1,'_')
        
    def _set_sentence(self, sentence):
        sentence = " ".join(sentence.split())
        self._sentence = sentence

    def get_C(self):
        return self._C

    def get_C_number(self):
        return self._C_number
        
    def get_W(self):
        return self._W
        
    def get_sentence(self):
        return self._sentence
    
    def get_grams(self):
        return self._grams
    
    def get_freqs(self):
        return self._freqs
    
    def get_score(self):
        return self._score
    
    def get_output(self):
        return self._output

    def get_output_str(self):
        return " ".join(self._output)
    
    def get_probability(self):
        return self._probability
    
