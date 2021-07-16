from library.algorithms.stemming.Stemmer.Context.Visitor.DontStemShortWord import DontStemShortWord
from library.algorithms.stemming.Stemmer.Context.Visitor.PrefixDisambiguator import PrefixDisambiguator

from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorPrefix import *
from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorSuffix import *
from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorInfix import *

class VisitorProvider(object):

    def __init__(self):
        self.visitors = []
        self.suffix_visitors = []
        self.infix_pisitors = []
        self.prefix_pisitors = []

        self.init_visitors()

    def init_visitors(self):
        self.visitors.append(DontStemShortWord())

        self.suffix_visitors.append(PrefixDisambiguator([DisambiguatorSuffixRuleAng()]))
        self.suffix_visitors.append(PrefixDisambiguator([DisambiguatorSuffixRuleMa()]))
        self.suffix_visitors.append(PrefixDisambiguator([DisambiguatorSuffixRuleMi()]))
        self.suffix_visitors.append(PrefixDisambiguator([DisambiguatorSuffixRuleI()]))
        self.suffix_visitors.append(PrefixDisambiguator([DisambiguatorSuffixRuleKa()]))



        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRuleMa()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRuleAk()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRuleAn()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRuleMak()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRuleMan()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRuleNi()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRuleTan()]))


        self.infix_pisitors.append(PrefixDisambiguator([DisambiguatorInfixUm()]))
        self.infix_pisitors.append(PrefixDisambiguator([DisambiguatorInfixIm()]))
        self.infix_pisitors.append(PrefixDisambiguator([DisambiguatorInfixAl()]))
        self.infix_pisitors.append(PrefixDisambiguator([DisambiguatorInfixAr()]))


    def get_visitors(self):
        return self.visitors

    def get_suffix_visitors(self):
        return self.suffix_visitors

    def get_prefix_visitors(self):
        return self.prefix_pisitors


    def get_infix_visitors(self):
        return self.infix_pisitors

