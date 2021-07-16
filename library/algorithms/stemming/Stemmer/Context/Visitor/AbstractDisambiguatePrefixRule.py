import re

class AbstractDisambiguatePrefixRule(object):
    """description of class"""

    def __init__(self):
        self.disambiguators = []

    def visit(self, context):
        result = None

        for disambiguator in self.disambiguators:
            result = disambiguator.disambiguate(context.current_word)
            if context.dictionary.contains(result):
                break

        if not result:
            return

        context.current_word = result

    def add_disambiguators(self, disambiguators):
        for disambiguator in disambiguators:
            self.add_disambiguator(disambiguator)

    def add_disambiguator(self, disambiguator):
        self.disambiguators.append(disambiguator)



