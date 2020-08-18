# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include, re_path  # add this

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
urlpatterns = [

    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='changepassword.html'), {'post_change_redirect': 'password_change_done'},name="password_change"),

    path("", include("authentication.urls")),  # add this
    path("", include("encuestas.urls")),  # add this
    #path('encuestas/', include('encuestas.urls')),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)