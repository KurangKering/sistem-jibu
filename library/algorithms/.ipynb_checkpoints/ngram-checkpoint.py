from copy import deepcopy
import re

class NonBasicFreqAlgorithm:
    
     def get_freq(self, input_string, word):
        word_len = len(word)
        ouut = []
        for i,c in enumerate(input_string):
            ouut.append(input_string[i:i+word_len])

        return sum(1 for x in ouut if x == word )
    
    
class BasicFreqAlgorithm:
    
    def get_freq(self, input_string, word):
        count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), input_string))
        return count


class BasicNGram:
    
    def __init__(self):
        self._freq_algorithm = BasicFreqAlgorithm()
    
    
    def execute(self, C, W):
        
        return self.get_ngram_with_freq(deepcopy(C), deepcopy(W))
    
    def get_freq(self, input_string, word):
        count = self._freq_algorithm.get_freq(input_string, word)
        return count

   
    def get_ngram_with_freq(self, C, W):
        self._C = C
        self._W = W
        
        
        
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
            
        
