import re

class Preprocessing:

    def __init__(self, sentences):
        self._cleaning(sentences)


    def _cleaning(self, sentences):
        cleaned = self._case_folding(sentences)
        cleaned = self._tokenizing(cleaned)
        cleaned = self._character_cleaning(cleaned)
        return self

    def _case_folding(self, sentences):
        lower = sentences.lower()
        self._case_folded = lower
        return lower

    def _tokenizing(self, sentences):
        token = sentences.split()
        self._tokenized = (token)
        return sentences

    def _character_cleaning(self, text):
        text = ' '.join(re.sub(r"(#\S+)|(@[A-Za-z0-9_]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(\d+)", " ", text).split())
        text = re.sub(r"\b[a-zA-Z]\b", "", text)
        text = " ".join(text.split())
        cleaned = text
        self._character_cleaned = cleaned
        return cleaned

    def get_case_folded(self):
        return self._case_folded

    def get_tokenized(self):
        return self._tokenized

    def get_character_cleaned(self):
        return self._character_cleaned