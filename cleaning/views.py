from django.shortcuts import render
from library.algorithms.cleaner import Preprocessing
from django.http import JsonResponse, HttpResponse
from data_uji.models import DataUji
# Create your views here.


def index(request):

    return render(request, 'cleaning/index.html')

def cleaning(request):
    updates_raw_data_uji = DataUji.objects.all().in_bulk()
    for key, data_uji in updates_raw_data_uji.items():
        cleaned_data = Preprocessing(data_uji.raw_data)
        data_uji.cleaned_data = cleaned_data.get_cleaned_sentence()

    updated = DataUji.objects.bulk_update(updates_raw_data_uji.values(), ['cleaned_data'], batch_size=100)

    cleaned_data_uji = DataUji.objects.all().values()
    cleaned_data_uji_list = []
    if (len(cleaned_data_uji) > 0):
        cleaned_data_uji_list = list(cleaned_data_uji)



    output = {
        'success': True,
        'cleaned_data_uji': cleaned_data_uji_list
    }

    return JsonResponse(output, safe=False)






