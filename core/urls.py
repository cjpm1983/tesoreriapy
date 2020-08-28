# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from adminplus.sites import AdminSitePlus
from django.shortcuts import redirect, reverse
from django.urls import path, include, re_path  # add this

from django.conf import settings
from django.conf.urls.static import static

import tesoreria

admin.site = AdminSitePlus()
admin.autodiscover()
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),  # add this
    path("", tesoreria.views.estadistica,name="home"),  # add this
    path('',include("tesoreria.urls"))
    #path("", include("tesoreria.urls")),  # add this

    #pippath("", include("encuestas.urls")),  # add this
    #path('tesoreria/', include('tesoreria.urls')),
    #path('encuestas/', include('encuestas.urls')),
    # path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    # path('password-change/', auth_views.PasswordChangeView.as_view(template_name='changepassword.html'), {'post_change_redirect': 'password_change_done'},name="password_change"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
