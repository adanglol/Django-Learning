from django.shortcuts import render
from .models import Question

# Create your views here.
from django.http import HttpResponse

# To use templates
# from django.template import loader

# Nah use shortcut its less bloat for tempplates
from django.shortcuts import render,get_object_or_404   

# returning a 404 not found lib
# from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # template = loader.get_template("polls/index.html")
    # context dictionary mapping temp var names to python obj
    context = {"latest_question_list" : latest_question_list}
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    # try:
    #     question = Question.objects.get(pk=question_id) 
    # except Question.DoesNotExist:
    #     return Http404("Question does not exist")
    # return render(request,'polls/detail.html',{'question':question})
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html",{"question":question})



    # return HttpResponse("You are looking at question %s" % question_id)

def results(request,question_id):
    response = "You are looking at the results of question %s."
    return HttpsResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You are voting on question %s" % question_id)
