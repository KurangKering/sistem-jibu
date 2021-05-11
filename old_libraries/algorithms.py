import os
import textdistance
import re
from copy import deepcopy


class ProbabilityScore:
    
    def calculate_probability(self, C, ngram_freq):
        
        gram, freq = ngram_freq
        lbigram, rbigram, trigram = gram
        freq_lbigram, freq_rbigram, freq_trigram = freq


        sigma_lbigram = [sum(x) for x in freq_lbigram]
        sigma_rbigram = [sum(x) for x in freq_rbigram]
        sigma_trigram = [sum(x) for x in freq_trigram]

        prob_lbigram = []
        prob_rbigram = []
        prob_trigram = []

        for x in range(len(C)):
            prob_array_lbigram = []
            prob_array_rbigram = []
            prob_array_trigram = []

            for y in range(len(C[x])):
                prob_single_lbigram = (freq_lbigram[x][y] + 0.01) / (sigma_lbigram[x] + 0.01 * len(C[x]))
                prob_array_lbigram.append(prob_single_lbigram)

                prob_single_rbigram = (freq_rbigram[x][y] + 0.01) / (sigma_rbigram[x] + 0.01 * len(C[x]))
                prob_array_rbigram.append(prob_single_rbigram)

                prob_single_trigram = (freq_trigram[x][y] + 0.01) / (sigma_trigram[x] + 0.01 * len(C[x]))
                prob_array_trigram.append(prob_single_trigram)

            prob_lbigram.append(prob_array_lbigram)
            prob_rbigram.append(prob_array_rbigram)
            prob_trigram.append(prob_array_trigram)
            
        return (prob_lbigram, prob_rbigram, prob_trigram)
        
    
    
    def calculate_score(self, C, probability, lambda_gram = (0.25, 0.25, 0.5)):
        
        prob_lbigram, prob_rbigram, prob_trigram = probability
         
        lambda_lbigram, lambda_rbigram, lambda_trigram = lambda_gram

        scores = []

        for x in range(len(C)):
            array = []
            for y in range(len(C[x])):
                score = (lambda_lbigram * prob_lbigram[x][y]) + (lambda_rbigram * prob_rbigram[x][y]) + (lambda_trigram * prob_trigram[x][y])
                array.append(score)
            scores.append(array)

        return scores
    
    def get_output(self, C, scores):
    
        output = []
        for x in range(len(C)):
            if (scores[x] == []):
                text = "-"
            else:
                max_index = (scores[x].index(max(scores[x])))
                text = C[x][max_index]

            output.append(text)

        return output

        

def get_words(kamus=1):
    
    #current_dir = globals()['_dh'][0]
    current_dir = os.path.dirname(os.path.realpath(__file__))
    kamus_file = ['kamus_indo.txt', 'kamus_makassar.txt']
    dictionaryFile = current_dir + '/data/' + kamus_file[kamus]
    if not os.path.isfile(dictionaryFile):
        raise RuntimeError('Dictionary file is missing. It seems that your installation is corrupted.')

    dictionaryContent = ''
    with open(dictionaryFile, 'r') as f:
        dictionaryContent = f.read()

    return dictionaryContent.split('\n')


class NGram:
    
    _C = []
    _W = []
    
    
    def __init__(self, C, W):
        self._C = C
        self._W = W
    
    def get_freq(self, input_string, word):
        count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), input_string))
        return count

    def get_freq_nub(self, input_string, word):
        word_len = len(word)
        ouut = []
        for i,c in enumerate(input_string):
            ouut.append(input_string[i:i+word_len])

        return sum(1 for x in ouut if x == word )
        
    def get_ngram_with_freq(self):
        out_lbigram = []
        out_rbigram = []
        out_trigram = []
        
        out_freq_lbigram = []
        out_freq_rbigram = []
        out_freq_trigram = []
        
        
        plain_text = " ".join(self._W)
        
        for x in range(1,len(self._W)-1):
            container_lbigram = []
            container_rbigram = []
            container_trigram = []
            
            container_freq_lbigram = []
            container_freq_rbigram = []
            container_freq_trigram = []
                
            for y in range(len(self._C[x-1])):
                lbigram = "{} {}".format(self._W[x-1], self._C[x-1][y])
                rbigram = "{} {}".format(self._C[x-1][y], self._W[x+1])
                trigram = "{} {} {}".format(self._W[x-1], self._C[x-1][y], self._W[x+1])
                
                freq_lbigram = self.get_freq(plain_text, lbigram)
                freq_rbigram = self.get_freq(plain_text, rbigram)
                freq_trigram = self.get_freq(plain_text, trigram)
                
                
                container_lbigram.append(lbigram)
                container_rbigram.append(rbigram)
                container_trigram.append(trigram)
                
                container_freq_lbigram.append(freq_lbigram)
                container_freq_rbigram.append(freq_rbigram)
                container_freq_trigram.append(freq_trigram)
            
            out_lbigram.append(container_lbigram)
            out_rbigram.append(container_rbigram)
            out_trigram.append(container_trigram)
            
            out_freq_lbigram.append(container_freq_lbigram)
            out_freq_rbigram.append(container_freq_rbigram)
            out_freq_trigram.append(container_freq_trigram)
            
        return [(out_lbigram, out_rbigram, out_trigram), (out_freq_lbigram, out_freq_rbigram, out_freq_trigram)]
            
        

class DamerauLevenshtein(object):
    
    _dict = None
    _max_op = 1
    def __init__(self, dictionary):
        self._dict = dictionary
        self._C = []
        self._W = []
    
    def get_C(self):
        return self._C
    
    def get_W(self):
        return self._W
    
    def process(self, text):
        
        words = text.split(' ')
        self.set_W(words)
        
        result = []
        
        for word in words:
            result.append(self.process_word(word))
        
        self.set_C(result)
        
        return result
    
    def set_C(self, damerau_output):
        self._C = [list(x.keys()) for x in damerau_output]
        
    def set_W(self, token):
        self._W = deepcopy(token)
        self._W.insert(0,'_')
        self._W.insert(len(token)+1,'_')
        
    def process_word(self, word):
        result = {}
        proceed = self.real_process(word)
        if proceed == []:
            return result
            
        result = {k: v for k, v in proceed if v <= self._max_op}
            
        return result
    
    def real_process(self, word):
        
        output = []
        checked_word = [x for x in self._dict.as_list() if x.startswith(word[0])]
        for dict_word in checked_word:
            num_of_process = self.singular_damerau(word, dict_word)
            if num_of_process is None:
                continue
            temp = (dict_word, num_of_process)
            output.append(temp)
        
        output = sorted(output, key=lambda tup: tup[1])
        
        return output
        
        
    def singular_damerau(self, word1, word2):
        damerau = textdistance.DamerauLevenshtein()
        num = damerau(word1, word2)
        return num
    

class CacheDamerauLevenshtein:
    
    def __init__(self, cache, delegate_damerau):
        self.cache = cache
        self.delegate_damerau = delegate_damerau
    
    def process(self, text):
        words = text.split(' ')
        result = []
        
        for word in words:
            result.append(self.process_word(word))
        
        return result
    

class ArrayDictionary(object):
    """description of class"""

    def __init__(self, words=None):
        self.words = []
        if words:
            self.add_words(words)
            
    def as_list(self):
        return self.words
    
    def contains(self, word):
        return word in self.words

    def count(self):
        return len(self.words)

    def add_words(self, words):
        """Add multiple words to the dictionary"""
        for word in words:
            self.add(word)

    def add(self, word):
        """Add a word to the dictionary"""
        if not word or word.strip() == '':
            return
        self.words.append(word)