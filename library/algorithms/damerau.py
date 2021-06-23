import jellyfish

class DamerauLevenshtein:

    _dict = None
    _max_op = 1

    def execute(self, dictionary, sentence):
        self._dict = dictionary
        result = self.process(sentence)
        print(result)
        return result

    def process(self, text):

        words = text.split(' ')
        result = []

        for word in words:
            result.append(self.process_word(word))

        return result

    def process_word(self, word):
        result = {}
        proceed = self.real_process(word)
        if proceed == []:
            return result

        result = {k: v for k, v in proceed if v <= self._max_op}

        return result

    def real_process(self, word):

        output = []
        # checked_word = [x for x in self._dict.as_list() if x.startswith(word[0])]
        panjang_word = len(word)
        batas_kecil = panjang_word - self._max_op
        batas_besar = panjang_word + self._max_op  

        checked_word = [x for x in self._dict if len(x) >= batas_kecil and len(x) <= batas_besar]
        for dict_word in checked_word:
            num_of_process = self.singular_damerau(word, dict_word)
            if num_of_process is None:
                continue
            temp = (dict_word, num_of_process)
            output.append(temp)

        output = sorted(output, key=lambda tup: tup[1])

        return output

    def singular_damerau(self, word1, word2):
        num = jellyfish.damerau_levenshtein_distance(word1, word2)
        return num


class CachedDamerauLevenshtein(DamerauLevenshtein):
    pass
