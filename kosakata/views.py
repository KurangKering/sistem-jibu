from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Kosakata
from django.core import serializers
from .forms import KosakataForm
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from tablib import Dataset
from .resources import KosakataResource
from django.db import connection

# Create your views here.

def index(request):
    return render(request, 'kosakata/index.html')


def menu_import(request):

    kosakata_list = Kosakata.objects.all()
    total_data = len(kosakata_list)
    context = {
        'total_data': total_data
    }
    return render(request, 'kosakata/menu_import.html', context)

def insert_kosakata(request):

    form = KosakataForm(request.POST)
    data = {}
    context = {'success': True}
    if form.is_valid():
        data = form.cleaned_data
        kosakata = Kosakata()
        kosakata.kata = data['kata']
        kosakata.arti_kata = data['arti_kata']
        kosakata.save()
       
    else:
        errors = form.errors
        context = {
            'success': False,
            'msg': errors
        }

    return JsonResponse(context, safe=False)

def update_kosakata(request):

    form = KosakataForm(request.POST)
    data = {}
    context = {'success': True}
    if form.is_valid():
        data = form.cleaned_data
        kosakata = Kosakata.objects.get(pk=request.POST.get('id'))
        kosakata.kata = data['kata']
        kosakata.arti_kata = data['arti_kata']
        kosakata.save()
       
    else:
        errors = form.errors
        context = {
            'success': False,
            'msg': errors
        }

    return JsonResponse(context, safe=False)


@csrf_exempt
def delete_kosakata(request):
    id_kosakata = request.POST.get('id')
    kosakata = Kosakata.objects.get(pk=id_kosakata)
    kosakata.delete()
    context = {
        'success': True,
        'msg': 'data successfully deleted'
    }

    return JsonResponse(context, safe=False)

@csrf_exempt
def json_single_kosakata(request):
    id_kosakata = request.POST.get('id')
    if (id_kosakata == None or id_kosakata == ''):
        return JsonResponse({'errors': ['id tidak boleh kosong']}, safe=False)

    kosakata = Kosakata.objects.get(pk=id_kosakata)
    serial = model_to_dict(kosakata)    
    return JsonResponse(serial, safe=False)

def import_kosakata(request):
    kosakata_resource = KosakataResource()
    dataset = Dataset()
    file = request.FILES['file']
    imported_kosakata = dataset.load(file.read())
    result = kosakata_resource.import_data(dataset, dry_run=True)

    if not result.has_errors():
        if request.POST.get('delete_all_data') == 'on':
            Kosakata.objects.all().delete()
            table_name = Kosakata.objects.model._meta.db_table

            sql = ""

            if (connection.vendor == 'sqlite'):
                sql = "DELETE FROM SQLite_sequence WHERE name='{}';".format(table_name)
            elif (connection.vendor == 'postgresql'):
                sequence = f"{table_name}_id_seq"
                sql = "ALTER SEQUENCE {} RESTART WITH 1;".format(sequence)


            with connection.cursor() as cursor:
                cursor.execute(sql)

        kosakata_resource.import_data(dataset, dry_run=False)
        context = {
            'success': True
        }
    else:
        context = {
            'success': False
        }

    return JsonResponse(context, safe=False)

def json_kosakata(request):
    kosakata = Kosakata.objects.all().values()
    kosakata_list = []
    if (len(kosakata) > 0):
        kosakata_list = list(kosakata)


    return JsonResponse(kosakata_list, safe=False)

