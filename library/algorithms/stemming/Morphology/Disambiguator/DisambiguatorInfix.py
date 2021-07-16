import re

class DisambiguatorInfixUm(object):
    
    def disambiguate(self, word):
        matches = re.match(r'^([a-z])um([a-z].*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)


class DisambiguatorInfixIm(object):
    
    def disambiguate(self, word):
        matches = re.match(r'^([a-z])im([a-z].*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)


class DisambiguatorInfixAl(object):
    
    def disambiguate(self, word):
        matches = re.match(r'^([a-z])al([a-z].*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)


class DisambiguatorInfixAr(object):
    
    def disambiguate(self, word):
        matches = re.match(r'^([a-z])ar([a-z].*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)

