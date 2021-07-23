from django.shortcuts import render
from library.algorithms.cleaner import Preprocessing
from django.http import JsonResponse, HttpResponse
from data_uji.models import DataUji
from kosakata.models import Kosakata
from library.algorithms.stemming.Stemmer.StemmerFactory import StemmerFactory
from library.algorithms.stemming.Dictionary.ModelDatabase import ModelDatabase
# Create your views here.


def index(request):
    updates_raw_data_uji = DataUji.objects.all().in_bulk()
    factory_stemmer = StemmerFactory()
    kamusDatabase = ModelDatabase(Kosakata, 'kata')
    stemmer = factory_stemmer.create_stemmer(False, kamusDatabase)

    for key, data_uji in updates_raw_data_uji.items():
        cleaned_data = Preprocessing(data_uji.raw_data)
        cleaned_data = cleaned_data.get_cleaned_sentence()
        data_uji.cleaned_data = cleaned_data
        data_uji.stemmed_data = stemmer.stem(cleaned_data)

    updated = DataUji.objects.bulk_update(updates_raw_data_uji.values(), ['cleaned_data', 'stemmed_data'], batch_size=100)

    return render(request, 'cleaning/index.html')


def cleaning(request):
    updates_raw_data_uji = DataUji.objects.all().in_bulk()
    factory_stemmer = StemmerFactory()
    kamusDatabase = ModelDatabase(Kosakata, 'kata')
    stemmer = factory_stemmer.create_stemmer(False, kamusDatabase)

    for key, data_uji in updates_raw_data_uji.items():
        cleaned_data = Preprocessing(data_uji.raw_data)
        cleaned_data = cleaned_data.get_cleaned_sentence()
        data_uji.cleaned_data = cleaned_data
        data_uji.stemmed_data = stemmer.stem(cleaned_data)

    updated = DataUji.objects.bulk_update(updates_raw_data_uji.values(), ['cleaned_data', 'stemmed_data'], batch_size=100)

    
    output = {
        'success': True,
    }

    return JsonResponse(output, safe=False)






