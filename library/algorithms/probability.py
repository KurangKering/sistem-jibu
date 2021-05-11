
class BasicProbability:
    
    def execute(self, C, gram_freq):
        probability = self.calculate(C, gram_freq)
        return probability
    
    def calculate(self, C, gram_freq):
        gram, freq = gram_freq
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