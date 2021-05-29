from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.contrib.messages import get_messages
from kosakata.models import Kosakata
from library.algorithms.cleaner import Preprocessing
from library.algorithms.factory import NormalisasiFactory
from library.algorithms.dictionary import DefaultDictionary, DatabaseDictionary
from data_uji.models import DataUji
# from old_libraries.algorithms import *

# Create your views here.
def index(request):

    return render(request, 'normalisasi/index.html')

def perhitungan(request):
    return render(request, 'normalisasi/perhitungan.html')

def bulk_normalize(request):
    cleaned_data = DataUji.objects.values_list()
    normalized_data = []
    factory = NormalisasiFactory()
    normalizer = factory.create_basic_normalizer(DatabaseDictionary(Kosakata, 'kata'))



    for x in (cleaned_data):
        normalized = normalizer.normalisasi(x[2])
        string_normalized = normalized.get_output_str()
        normalized_data.append([x[0], x[2], string_normalized])

    output = {
        'success': True,
        'normalized_data': normalized_data
    }

    return JsonResponse(output, safe=False)


def normalize(request):
    raw_inputan = request.POST.get('inputan', '')

    if raw_inputan == "":
        return redirect(index)

    preprocessed_object = Preprocessing(raw_inputan)
    factory = NormalisasiFactory()
    normalizer = factory.create_basic_normalizer(DatabaseDictionary(Kosakata, 'kata'))
    hasil_normalisasi = normalizer.normalisasi(preprocessed_object.get_cleaned_sentence())

    hasil_damerau = hasil_normalisasi.get_C_number()
    jumlah_damerau = [len(x)+1 for x in hasil_damerau]
    C = hasil_normalisasi.get_C()
    W = hasil_normalisasi.get_W()
    lbigram, rbigram, trigram = hasil_normalisasi.get_grams()
    lfreq, rfreq, trifreq = hasil_normalisasi.get_freqs()
    score = hasil_normalisasi.get_score()
    output_string = hasil_normalisasi.get_output_str()
    cleaned_sentence = hasil_normalisasi.get_sentence()
    array_cleaned_sentence = hasil_normalisasi.get_sentence().split(' ')

    ziped_freq_gram = []
    for x in range(len(array_cleaned_sentence)):
        ziped_freq_gram.append([len(lbigram[x])+1, array_cleaned_sentence[x], zip(C[x], lbigram[x], rbigram[x], trigram[x], lfreq[x], rfreq[x], trifreq[x], score[x])])
        

    content = {
        'input':raw_inputan,
        'cleaned_input': cleaned_sentence,
        'output':output_string,
        'damerau': hasil_damerau,
        'array_inputan':array_cleaned_sentence,
        'inputan_damerau': zip(array_cleaned_sentence, hasil_damerau, jumlah_damerau),
        'hasil_gram': ziped_freq_gram,
    }

    return render(request, 'normalisasi/summary.html', content)




def old_normalize(request):
    inputan = request.POST.get('inputan', '')

    text = ""
    if inputan == "":
        return redirect(index)

    sentence = " ".join(inputan.lower().split())


    words = get_words()
    dictionary = ArrayDictionary(words)
    damerau = DamerauLevenshtein(dictionary)
    hasil_damerau = damerau.process(sentence)
    
    C = damerau.get_C()
    W = damerau.get_W()

    ngram = NGram(C,W)
    gram_freq= ngram.get_ngram_with_freq()
    nnngram, freq = gram_freq

    lbigram, rbigram, trigram = nnngram
    lfreq, rfreq, trifreq = freq


    pro_score = ProbabilityScore()
    probability = pro_score.calculate_probability(C, gram_freq)
    score = pro_score.calculate_score(C, probability)
    output = pro_score.get_output(C, score)
    
    text = " ".join(output)

    array_inputan = inputan.split(' ')
    jumlah_damerau = [len(x)+1 for x in hasil_damerau]

    ziped_freq_gram = []
    for x in range(len(array_inputan)):
        ziped_freq_gram.append([len(lbigram[x])+1, array_inputan[x], zip(C[x], lbigram[x], rbigram[x], trigram[x], lfreq[x], rfreq[x], trifreq[x], score[x])])
        

    content = {
        'input':inputan,
        'cleaned_input': inputan,
        'output':text,
        'damerau': hasil_damerau,
        'array_inputan':array_inputan,
        'inputan_damerau': zip(array_inputan, hasil_damerau, jumlah_damerau),
        'hasil_gram': ziped_freq_gram,
    }

    return render(request, 'normalisasi/summary.html', content)

