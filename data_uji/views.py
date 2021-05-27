from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import DataUji
from django.core import serializers
from .forms import DataUjiForm
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from tablib import Dataset
from .resources import DataUjiResource
from django.db import connection
# Create your views here.

def index(request):
    return render(request, 'data_uji/index.html')


def menu_import(request):

    data_uji_list = DataUji.objects.all()
    total_data = len(data_uji_list)
    context = {
        'total_data': total_data
    }
    return render(request, 'data_uji/menu_import.html', context)

def insert_data_uji(request):

    form = DataUjiForm(request.POST)
    data = {}
    context = {'success': True}
    if form.is_valid():
        data = form.cleaned_data
        data_uji = DataUji()
        data_uji.raw_data = data['raw_data']
        data_uji.cleaned_data = ''
        data_uji.save()
       
    else:
        errors = form.errors
        context = {
            'success': False,
            'msg': errors
        }

    return JsonResponse(context, safe=False)

def update_data_uji(request):

    form = DataUjiForm(request.POST)
    data = {}
    context = {'success': True}
    if form.is_valid():
        data = form.cleaned_data
        data_uji = DataUji.objects.get(pk=request.POST.get('id'))
        data_uji.raw_data = data['raw_data']
        data_uji.save()
       
    else:
        errors = form.errors
        context = {
            'success': False,
            'msg': errors
        }

    return JsonResponse(context, safe=False)


@csrf_exempt
def delete_data_uji(request):
    id_data_uji = request.POST.get('id')
    data_uji = DataUji.objects.get(pk=id_data_uji)
    data_uji.delete()
    context = {
        'success': True,
        'msg': 'data successfully deleted'
    }

    return JsonResponse(context, safe=False)

@csrf_exempt
def json_single_data_uji(request):
    id_data_uji = request.POST.get('id')
    if (id_data_uji == None or id_data_uji == ''):
        return JsonResponse({'errors': ['id tidak boleh kosong']}, safe=False)

    data_uji = DataUji.objects.get(pk=id_data_uji)
    serial = model_to_dict(data_uji)    
    return JsonResponse(serial, safe=False)

def import_data_uji(request):
    data_uji_resource = DataUjiResource()
    dataset = Dataset()
    file = request.FILES['file']
    imported_data_uji = dataset.load(file.read())
    result = data_uji_resource.import_data(dataset, dry_run=True)

    if not result.has_errors():
        if request.POST.get('delete_all_data') == 'on':
            DataUji.objects.all().delete()
            table_name = DataUji.objects.model._meta.db_table
            
            sql = ""
            if (connection.vendor == 'sqlite'):
                sql = "DELETE FROM SQLite_sequence WHERE name='{}';".format(table_name)
            elif (connection.vendor == 'postgresql'):
                sequence = f"{table_name}_id_seq"
                sql = "ALTER SEQUENCE {} RESTART WITH 1;".format(sequence)


            with connection.cursor() as cursor:
                cursor.execute(sql)

        data_uji_resource.import_data(dataset, dry_run=False)
        context = {
            'success': True
        }
    else:
        context = {
            'success': False
        }

    return JsonResponse(context, safe=False)

def json_data_uji(request):
    data_uji = DataUji.objects.all().values()
    data_uji_list = []
    if (len(data_uji) > 0):
        data_uji_list = list(data_uji)


    return JsonResponse(data_uji_list, safe=False)

