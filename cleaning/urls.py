from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="cleaning/index"),
    path('cleaning', views.cleaning, name="cleaning/cleaning"),
]