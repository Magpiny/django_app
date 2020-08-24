from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, Http404, render
from django.urls import reverse
from .models import Question, Choice

# Create your views here.


#Get questions and display them
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

#Show specific questions and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)

    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    return render(request, 'polls/details.html', {'question':question}) 

# Get questions and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})


def vote(request, question_id):
    #print(request.POST(choice))
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form
        return render(request, 'polls/details.html', {
            'question':question,
            'error_message':"You didn't select a choice! ",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #Always return a HttpResponseRedirect after a successfully dealing
        #with  a POST data. This prevents data from being posted twice if a
        #if a user hits the back button
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
    