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
from encuestas.forms import UserProfileForm, UserProfileChangeForm


@login_required(login_url="/login/")
def index(request):
    #up = UserProfile.objects.get(user = request.user)
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    # form = UserProfileForm(instance=request.user)
    # if ('email' in request.POST):
    #     form = UserProfileForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #
    #         render(request,str(form.errors))

    load_template = request.path.split('/')[-1]
    #html_template = loader.get_template(load_template)
    if load_template == 'profile.html':
        try:
            profile = request.user
        finally:
            if request.method == 'POST':
                form = UserProfileForm(request.POST, request.FILES, instance=profile)
                #form = UserProfileChangeForm(request.POST, request.FILES, instance=profile)
                if form.is_valid():
                    form.save()
                    #return render(request, load_template, {'form': form})
                    return redirect(load_template)

            else:
                form = UserProfileForm(instance=profile)
                return render(request,load_template, {'form':form})



    context = {}
    context = {'form': form}
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
