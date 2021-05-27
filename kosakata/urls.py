from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="kosakata/index"),
    path('menu_import', views.menu_import, name="kosakata/menu_import"),
    path('json_kosakata', views.json_kosakata, name="kosakata/json_kosakata"),
    path('insert_kosakata', views.insert_kosakata, name="kosakata/insert_kosakata"),
    path('update_kosakata', views.update_kosakata, name="kosakata/update_kosakata"),
    path('delete_kosakata', views.delete_kosakata, name="kosakata/delete_kosakata"),
    path('import_kosakata', views.import_kosakata, name="kosakata/import_kosakata"),
    path('json_single_kosakata', views.json_single_kosakata, name="kosakata/json_single_kosakata"),
]