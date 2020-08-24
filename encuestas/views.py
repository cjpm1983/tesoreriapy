from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice
from django.shortcuts import get_object_or_404, get_list_or_404, render

##de APP
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from encuestas.models import UserProfile
from encuestas.forms import UserProfileForm, UserProfileChangeForm




    # return HttpResponse(output)

class IndexView(generic.ListView):
    template_name = 'encuestas/index.html'
    context_object_name = 'Questions'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'encuestas/details.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'encuestas/results.html'
    # Create your views here.


'''    
    def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = '<br> '.join(['<a href="/%d">%s</a>' % (q.id, q.question_text) for q in latest_question_list])

    Questions = get_list_or_404(Question)

    return render(request, 'encuestas/index.html', {'Questions': Questions})
    # return HttpResponse(output)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'encuestas/details.html', {'question':question})
    #return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'encuestas/results.html', {'question': question})

'''


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'encuestas/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('encuestas:results', args=(question.id,)))


###De APP


@login_required(login_url="/login/")
def index(request):
    # up = UserProfile.objects.get(user = request.user)
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
    context = {}
    load_template = request.path.split('/')[-1]
    # html_template = loader.get_template(load_template)
    if load_template == 'profile.html':
        try:
            profile = request.user
        finally:
            if request.method == 'POST':
                #form = UserProfileForm(request.POST, request.FILES, instance=profile)
                form = UserProfileChangeForm(request.POST, request.FILES, instance=profile)
                if form.is_valid():
                    form.save()
                    # return render(request, load_template, {'form': form})
                    return redirect(load_template)

            else:
                form = UserProfileChangeForm(instance=profile)
                return render(request, load_template, {'form': form})
        context = {'form': form}


    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('error-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('error-500.html')
        return HttpResponse(html_template.render(context, request))
