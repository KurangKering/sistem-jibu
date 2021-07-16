from .normalizer import DamerauNormalizer


class NormalisasiFactory:

    def create_basic_normalizer(self, dictionary):

        basic =  DamerauNormalizer(dictionary)
        return basic