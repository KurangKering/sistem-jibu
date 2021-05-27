from .helper import get_words

class DefaultDictionary(object):
    """description of class"""

    def __init__(self, words=None):
        self.words = []
        words = get_words()
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

class DatabaseDictionary(object):

    def __init__(self, model, field):
        self.words = model.objects.values_list(field, flat=True)

    def as_list(self):
        return self.words

