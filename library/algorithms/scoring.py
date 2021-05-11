class BasicScoring:
    
    def execute(self, C, probability, lambda_gram=(0.25, 0.25, 0.5)):
        
        score = self.calculate(C, probability, lambda_gram)
        output = self.get_output(C, score)
        return (score, output)
        
    def calculate(self, C, probability, lambda_gram = (0.25, 0.25, 0.5)):
        
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
