# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from django.conf.urls.static import static

#importante importar desde . las views
from . import views

#muy importante esta linea
#app_name = 'tesoreria'

urlpatterns = [
    #path('tesoreria/obrero  detail', views.IndexView.as_view(), name='obrero'),
    path('tesoreria/<int:pk>/obrero', views.DetailView.as_view(), name='obrero'),
    #path('tesoreria/<str:tipo>/<int:id>/exportar', views.exportar, name = 'exportar'),
    path('tesoreria/exportar', views.exportar, name = 'exportar')
    #path('', views.estadisticas, name='home')
    #path('', views.estadistica, name='home'),
    #path('encuestas/estadisticas',views.estadisticas)
]
