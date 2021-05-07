from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="normalisasi/index"),
    path('normalize', views.normalize, name="normalisasi/normalize")
]