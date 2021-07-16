import re

class Preprocessing:

    def __init__(self, sentence):
        self._cleaning(sentence)


    def _cleaning(self, sentence):
        cleaned_sentence = self._case_folding(sentence)
        cleaned_sentence = self._tokenizing(cleaned_sentence)
        cleaned_sentence = self._character_cleaning(cleaned_sentence)
        return self

    def _case_folding(self, sentence):
        lower = sentence.lower()
        self._case_folded = lower
        return lower

    def _tokenizing(self, sentence):
        token = sentence.split()
        self._tokenized = (token)
        return sentence

    def _character_cleaning(self, sentence):
        sentence = ' '.join(re.sub(r"(#\S+)|(@[A-Za-z0-9_]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(\d+)", " ", sentence).split())
        sentence = re.sub(r"\b[a-zA-Z]\b", "", sentence)
        sentence = " ".join(sentence.split())
        cleaned = sentence
        self._cleaned_sentence = cleaned
        return cleaned
    

    def get_case_folded(self):
        return self._case_folded

    def get_tokenized(self):
        return self._tokenized

    def get_cleaned_sentence(self):
        return self._cleaned_sentence