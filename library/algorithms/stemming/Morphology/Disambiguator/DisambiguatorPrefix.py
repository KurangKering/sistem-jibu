import re

class DisambiguatorPrefixRuleMa(object):
    
    def disambiguate(self, word):
        matches = re.match(r'^ma(.*)$', word)
        if matches:
            return matches.group(1)

class DisambiguatorPrefixRuleAk(object):
    
    def disambiguate(self, word):
        matches = re.match(r'^ak(.*)$', word)
        if matches:
            return matches.group(1)

class DisambiguatorPrefixRuleAn(object):
    
    def disambiguate(self, word):
        matches = re.match(r'^an(.*)$', word)
        if matches:
            return matches.group(1)

class DisambiguatorPrefixRuleMak(object):
    
    def disambiguate(self, word):
        matches = re.match(r'^mak(.*)$', word)
        if matches:
            return matches.group(1)

class DisambiguatorPrefixRuleMan(object):
    
    def disambiguate(self, word):
        matches = re.match(r'^man(.*)$', word)
        if matches:
            return matches.group(1)

class DisambiguatorPrefixRuleNi(object):
    
    def disambiguate(self, word):
        matches = re.match(r'^ni(.*)$', word)
        if matches:
            return matches.group(1)

class DisambiguatorPrefixRuleTan(object):
    
    def disambiguate(self, word):
        matches = re.match(r'^tan(.*)$', word)
        if matches:
            return matches.group(1)
