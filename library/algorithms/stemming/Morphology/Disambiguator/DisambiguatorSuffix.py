import re

class DisambiguatorSuffixRuleI(object):
    
    def disambiguate(self, word):
        matches = re.match(r'^([a-z].*)i$', word)
        if matches:
            return matches.group(1)

class DisambiguatorSuffixRuleAng(object):
    
    def disambiguate(self, word):
        matches = re.match(r'^([a-z].*)ang$', word)
        if matches:
            return matches.group(1)

class DisambiguatorSuffixRuleMa(object):
    
    def disambiguate(self, word):
        matches = re.match(r'^([a-z].*)ma$', word)
        if matches:
            return matches.group(1)


class DisambiguatorSuffixRuleMi(object):
    
    def disambiguate(self, word):
        matches = re.match(r'^([a-z].*)mi$', word)
        if matches:
            return matches.group(1)


class DisambiguatorSuffixRuleKa(object):
    
    def disambiguate(self, word):
        matches = re.match(r'^([a-z].*)mi$', word)
        if matches:
            return matches.group(1)

