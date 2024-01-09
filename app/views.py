from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse


def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('insertion of topic is done successfully')


    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('insertion of webpage is done successfully')

    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    EFAO=AccessRecordForm()
    d={'EFAO':EFAO}
    if request.method=='POST':
        ARDO=AccessRecordForm(request.POST)
        if ARDO.is_valid():
            ARDO.save()
            return HttpResponse('accessrecord data is inserted successfully')

    return render(request,'insert_accessrecord.html',d)






