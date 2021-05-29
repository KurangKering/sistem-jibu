from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="normalisasi/index"),
    path('perhitungan', views.perhitungan, name="normalisasi/perhitungan"),
    path('normalize', views.normalize, name="normalisasi/normalize"),
    path('bulk_normalize', views.bulk_normalize, name="normalisasi/bulk_normalize"),
]