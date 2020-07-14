from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.


def index(request):
    q_list = Question.objects.order_by('pub_date')[:5]
    context = {'latest_question_list': q_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(id = question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    

def results(request, question_id): # 투표 결과 페이지
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def votes(request, question_id): # 투표 페이지
     return HttpResponse("You're voting on question %s." % question_id)
