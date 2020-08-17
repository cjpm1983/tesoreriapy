from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice
from django.shortcuts import get_object_or_404, get_list_or_404, render


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
