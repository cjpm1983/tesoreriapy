# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from encuestas.models import UserProfile
from encuestas.forms import UserProfileForm, MyUserForm

@login_required(login_url="/login/")
def index(request):
    #up = UserProfile.objects.get(user = request.user)
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    #up = UserProfile.objects.get(user=request.user)
    #form = UserProfileForm(request.POST, instance=up)
    #form2 = MyUserForm(request.POST, instance=up.user)
    context = {}
    #context = {"userprofile": up, 'form': form, 'fomr2': form2}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))
