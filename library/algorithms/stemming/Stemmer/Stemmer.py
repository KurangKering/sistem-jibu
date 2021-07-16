import re
from library.algorithms.stemming.Stemmer.Context.Visitor.VisitorProvider import VisitorProvider
from library.algorithms.stemming.Stemmer.Filter import TextNormalizer
from library.algorithms.stemming.Stemmer.Context.Context import Context

class Stemmer(object):
    """Indonesian Stemmer.
    Nazief & Adriani, CS Stemmer, ECS Stemmer, Improved ECS.

    @link https://github.com/sastrawi/sastrawi/wiki/Resources
    """
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.visitor_provider = VisitorProvider()

    def get_dictionary(self):
        return self.dictionary

    def stem(self, text):
        """Stem a text string to its common stem form."""
        normalizedText = TextNormalizer.normalize_text(text)

        words = normalizedText.split(' ')
        stems = []

        for word in words:
            stems.append(self.stem_word(word))

        return ' '.join(stems)

    def stem_word(self, word):
        """Stem a word to its common stem form."""
        return self.stem_singular_word(word)

    def stem_singular_word(self, word):
        """Stem a singular word to its common stem form."""
        context = Context(word, self.dictionary, self.visitor_provider)
        context.execute()

        return context.result

