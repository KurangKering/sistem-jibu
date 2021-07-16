import jellyfish
import time
class DamerauLevenshtein:

    _dict = None
    _max_op = 1

    def execute(self, dictionary, sentence):
        start = time.time()
        self._dict = dictionary
        result = self.process(sentence)
        stop = time.time()
        print(f'waktu eksekusi : {stop - start}')
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

        condition = True
        count = 0
        while (condition):
            result = {k: v for k, v in proceed if v == count}

            condition = (result == {}) and (count < self._max_op)
            count = count + 1

        return result

    def real_process(self, word):

        output = []
        batas_bawah = len(word) - self._max_op
        batas_atas = len(word) + self._max_op
        checked_word = {x:x for x in self._dict if len(x) >= batas_bawah and len(x) <= batas_atas }
        for dict_word in checked_word:
            num_of_process = self.singular_levenshtein(word, dict_word)
            if num_of_process is None:
                continue
            temp = (dict_word, num_of_process)
            output.append(temp)

        output = sorted(output, key=lambda tup: tup[1])

        return output

    def singular_levenshtein(self, word1, word2):
        num = jellyfish.damerau_levenshtein_distance(word1, word2)
        return num

