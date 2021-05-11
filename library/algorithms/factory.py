from .normalizer import BasicNormalizer


class NormalisasiFactory:

    def create_basic_normalizer(self, dictionary):

        basic =  BasicNormalizer(dictionary)
        return basic