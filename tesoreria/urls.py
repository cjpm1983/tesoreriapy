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
app_name = 'tesoreria'

urlpatterns = [
    #path('', views.estadisticas, name='home')
    path('', views.estadisticas, name='estadisticas'),
    #path('encuestas/estadisticas',views.estadisticas)
]
