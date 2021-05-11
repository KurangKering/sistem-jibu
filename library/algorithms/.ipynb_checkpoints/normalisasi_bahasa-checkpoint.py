from . import damerau
from . import dictionary
from . import ngram
from . import probability
from . import scoring
from . import scoring
from . import helper
from copy import deepcopy



class BasicNormalisasi:
    
    _C = []
    _W = []
    _sentences = ""
    _score = []
    _probability = []
    _output = ""
    
    def __init__(self, words):
        self._algorithm = Normalisasi()
        self._execute(words)
        
    def _execute(self, words):
        result = self._algorithm.execute(words)
        self._C = result.get_C()
        self._W = result.get_W()
        self._sentences = result.get_sentences()
        self._score = result.get_score()
        self._probability = result.get_probability()
        self._output = result.get_output()
        

    def get_C(self):
        return self._C
        
    def get_W(self):
        return self._W
        
    def get_sentences(self):
        return self._sentences
    
    def get_score(self):
        return self._score
    
    def get_probability(self):
        return self._probability
    
    def get_output(self):
        return self._output
        

class Normalisasi:
    
    _C = []
    _W = []
    _sentences = ""
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
    
    def __init__(self):
        words = helper.get_words()
        self._dictionary = dictionary.ArrayDictionary(words)
        self._damerau_alg = damerau.DamerauLevenshtein()
        self._ngram_alg = ngram.BasicNGram()
        self._probability_alg = probability.BasicProbability()
        self._scoring_alg = scoring.BasicScoring()
    
    def execute(self, words):
        self._set_sentences(words)
        self._set_W(self._sentences)
        
        damerau = self._damerau_alg.execute(self._dictionary, self._sentences)
        self._set_C(damerau)
        self._grams, self._freqs = self._ngram_alg.execute(self._C, self._W)
        self._probability =  self._probability_alg.execute(self._C, (self._grams, self._freqs))
        self._score, self._output = self._scoring_alg.execute(self._C, self._probability)
        
        return self
    
    def _set_C(self, C):
        self._C =  [list(x.keys()) for x in C]
        
    def _set_W(self, sentences):
        token = deepcopy(sentences.split())
        self._W = deepcopy(token)
        self._W.insert(0,'_')
        self._W.insert(len(token)+1,'_')
        
    def _set_sentences(self, sentences):
        sentences = " ".join(sentences.split())
        self._sentences = sentences
    
    def get_C(self):
        return self._C
        
    def get_W(self):
        return self._W
        
    def get_sentences(self):
        return self._sentences
    
    def get_grams(self):
        return self._grams
    
    def get_score(self):
        return self._score
    
    def get_output(self):
        return self._output
    
    def get_probability(self):
        return self._probability
        
    
    
    
    
    
        