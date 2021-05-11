import os

def get_words(kamus=1):
    
    #current_dir = globals()['_dh'][0]
    current_dir = os.path.dirname(os.path.realpath(__file__))
    kamus_file = ['kamus_indo.txt', 'kamus_makassar.txt']
    dictionaryFile = current_dir + '/data/' + kamus_file[kamus]
    if not os.path.isfile(dictionaryFile):
        raise RuntimeError('Dictionary file is missing. It seems that your installation is corrupted.')

    dictionaryContent = ''
    with open(dictionaryFile, 'r') as f:
        dictionaryContent = f.read()

    return dictionaryContent.split('\n')
