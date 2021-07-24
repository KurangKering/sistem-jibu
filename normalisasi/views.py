from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.contrib.messages import get_messages
from kosakata.models import Kosakata
from library.algorithms.cleaner import Preprocessing
from library.algorithms.factory import NormalisasiFactory
from library.algorithms.dictionary import DefaultDictionary, DatabaseDictionary
from data_uji.models import DataUji
from django.views.decorators.csrf import csrf_exempt
from library.algorithms.stemming.Stemmer.StemmerFactory import StemmerFactory

from library.algorithms.stemming.Dictionary.ModelDatabase import ModelDatabase

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
    factory_stemmer = StemmerFactory()
    kamusDatabase = ModelDatabase(Kosakata, 'kata')
    stemmer = factory_stemmer.create_stemmer(False, kamusDatabase)
    cleaned_data = preprocessed_object.get_cleaned_sentence()
    stemmed_data = stemmer.stem(cleaned_data)
    content = reusable_normalize(stemmed_data)
    content['input'] = raw_inputan
    content['stemmed_data'] = stemmed_data

    content['inputan_levenshtein'] = zip(content['array_cleaned_sentence'], content['hasil_levensthein'], content['jumlah_levenshtein'])

    return render(request, 'normalisasi/summary.html', content)


@csrf_exempt
def ajax_normalize(request):
    id_data_uji =request.POST.get('id')
    option =request.POST.get('option')

    data_uji = None
    if (option == 'next'):
        try:
            data_uji = DataUji.objects.filter(id__gt=id_data_uji).order_by("id")[0:1].get()
            id_data_uji = data_uji.id
        except DataUji.DoesNotExist:
            pass

    elif (option == 'direct'):
        data_uji = DataUji.objects.get(pk=int(id_data_uji))

    elif (option == 'prev'):
        try:
            data_uji = DataUji.objects.filter(id__lt=id_data_uji).order_by("-id")[0:1].get()
            id_data_uji = data_uji.id

        except DataUji.DoesNotExist:
            pass

    if (data_uji == None):
        content = {
            'success' : False,
        }
    else:
        raw_inputan = data_uji.cleaned_data
        content = reusable_normalize(raw_inputan)
        content['success'] = True
        content['id_data_uji'] = id_data_uji
        content['inputan_levenshtein'] = list(zip(content['array_cleaned_sentence'], content['hasil_levensthein'], content['jumlah_levenshtein']))

    return JsonResponse(content, safe=False)


def reusable_normalize(inputan):

    factory = NormalisasiFactory()
    normalizer = factory.create_basic_normalizer(DatabaseDictionary(Kosakata, 'kata'))
    hasil_normalisasi = normalizer.normalisasi(inputan)

    hasil_levensthein = hasil_normalisasi.get_C_number()
    jumlah_levenshtein = [len(x)+1 for x in hasil_levensthein]
    cleaned_sentence = hasil_normalisasi.get_sentence()
    array_cleaned_sentence = hasil_normalisasi.get_sentence().split(' ')


    content = {
        'cleaned_input': cleaned_sentence,
        'array_cleaned_sentence': array_cleaned_sentence,
        'hasil_levensthein': hasil_levensthein,
        'jumlah_levenshtein': jumlah_levenshtein,

    }

    return content
