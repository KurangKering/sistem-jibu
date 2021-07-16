from library.algorithms.stemming.Stemmer.ConfixStripping.PrecedenceAdjustmentSpecification \
   import PrecedenceAdjustmentSpecification

class Context(object):
    """Stemming Context using Nazief and Adriani, CS, ECS, Improved ECS"""

    def __init__(self, original_word, dictionary, visitor_provider):
        self.original_word = original_word
        self.current_word = original_word
        self.dictionary = dictionary
        self.visitor_provider = visitor_provider

        self.process_is_stopped = False
        self.visitors = []
        self.suffix_visitors = []
        self.prefix_pisitors = []
        self.infix_pisitors = []
        self.result = ''

        self.init_visitors()

    def init_visitors(self):
        self.suffix_visitors = self.visitor_provider.get_suffix_visitors()
        self.prefix_pisitors = self.visitor_provider.get_prefix_visitors()
        self.infix_pisitors = self.visitor_provider.get_infix_visitors()

    def stopProcess(self):
        self.process_is_stopped = True

    def execute(self):
        """Execute stemming process; the result can be retrieved with result"""

        #step 1 - 5
        self.start_stemming_process()

        #step 6
        if self.dictionary.contains(self.current_word):
            self.result = self.current_word
        else:
            self.result = self.original_word

    def start_stemming_process(self):

        #step 1
        if self.dictionary.contains(self.current_word):
            return

        self.accept_visitors(self.visitors)
        if self.dictionary.contains(self.current_word):
            return

        #step 2, 3
        self.remove_suffixes()
        if self.dictionary.contains(self.current_word):
            return

        #step 4, 5
        self.remove_prefixes()
        if self.dictionary.contains(self.current_word):
            return
        
        #step 4, 5
        self.remove_infixes()
        if self.dictionary.contains(self.current_word):
            return

    def remove_prefixes(self):
        self.accept_visitors(self.suffix_visitors)

    def remove_suffixes(self):
        self.accept_visitors(self.suffix_visitors)

    def remove_infixes(self):
        self.accept_visitors(self.infix_pisitors)

    def accept(self, visitor):
        visitor.visit(self)

    def accept_visitors(self, visitors):
        for visitor in visitors:
            self.accept(visitor)
            if self.dictionary.contains(self.current_word):
                return self.current_word
            if self.process_is_stopped:
                return self.current_word

