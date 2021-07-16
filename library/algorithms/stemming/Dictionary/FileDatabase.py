import os
class FileDatabase(object):
    """description of class"""


    def get_kamus(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        dictionaryFile = current_dir + '\..\..\data\kamus_makassar.txt'
        if not os.path.isfile(dictionaryFile):
            print(dictionaryFile)
            raise RuntimeError('Dictionary file is missing. It seems that your installation is corrupted.')

        dictionaryContent = ''
        with open(dictionaryFile, 'r') as f:
            dictionaryContent = f.read()

        return dictionaryContent.split('\n')



