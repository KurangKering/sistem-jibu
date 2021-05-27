from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="data_uji/index"),
    path('menu_import', views.menu_import, name="data_uji/menu_import"),
    path('json_data_uji', views.json_data_uji, name="data_uji/json_data_uji"),
    path('insert_data_uji', views.insert_data_uji, name="data_uji/insert_data_uji"),
    path('update_data_uji', views.update_data_uji, name="data_uji/update_data_uji"),
    path('delete_data_uji', views.delete_data_uji, name="data_uji/delete_data_uji"),
    path('import_data_uji', views.import_data_uji, name="data_uji/import_data_uji"),
    path('json_single_data_uji', views.json_single_data_uji, name="data_uji/json_single_data_uji"),
]