#from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'encuestas'

urlpatterns = [
    #path('', views.index, name='home'),

    #path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done'),
    #path('password-change/', auth_views.PasswordChangeView.as_view(template_name='changepassword.html'),{'post_change_redirect': 'password_change_done'},name="password_change"),

    path('encuestas/', views.IndexView.as_view(), name='encuestas'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    ##de APP
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),


]
'''
path('', views.index, name='index'),
# ex: /polls/5/
path('<int:question_id>/', views.detail, name='detail'),
# ex: /polls/5/results/
path('<int:question_id>/results/', views.results, name='results'),
# ex: /polls/5/vote/
path('<int:question_id>/vote/', views.vote, name='vote'),
'''