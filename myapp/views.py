from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import *
from .forms import *

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import json
import sys


# Create html as variable your views here.
def index(request):
    #return HttpResponse("CINS465 Hello World")
    return render(request, 'index.html', {"world_template":"Ticket"})

def map(request):
    if request.method == 'POST':
        form = Event_Form(request.POST)
        if form.is_valid():
            event = Event_Model(
                name=form.cleaned_data['name'],
                start_date=form.cleaned_data['start_date'],
                end_date=form.cleaned_data['end_date'],
                location=form.cleaned_data['location'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data['image'],
                # longitude=request.POST['lat'],
                # latitude=request.POST['lng'],
            )
            event.save()
            form = Event_Form()
    else:
        form = Event_Form()

    event_list = Event_Model.objects.all()
    context = {
        "event_list":event_list,
        "form":form
        }
    return render(request, 'map.html', context)

def chat(request):
    if request.method == 'POST':
        json_data = request.POST.get('url')
        print(json_data)
        return HttpResponse("post request success")

    current_user_id = request.user.id
    context = {
        "current_user_id":current_user_id,
        }
    return render(request, 'chat.html', context)

def event(request):
    return render(request, 'event.html')

@csrf_exempt
def survey_api(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            #print(json_data['data'])
            surv = Survey_Model(survey=json_data['survey'])
            surv.save()
            return HttpResponse("hello")
        except:
            return HttpResponse("Unexpected error:"+str(sys.exc_info()[0]))
    if request.method == "PUT":
        json_data = json.loads(request.body)
        try:
            surv = Survey_Model.objects.get(pk=json_data['id'])
            surv.survey = json_data['survey']
            surv.save()

            #print(json_data['data'])
            return HttpResponse("hello")
        except:
            return HttpResponse("Unexpected error:"+str(sys.exc_info()[0]))
    if request.method == "DELETE":
        json_data = json.loads(request.body)
        try:
            surv = Survey_Model.objects.get(pk=json_data['id'])
            surv.delete()
            #print(json_data['data'])
            return HttpResponse("hello")
        except:
            return HttpResponse("Unexpected error:"+str(sys.exc_info()[0]))
    if request.method == 'GET':
        survey_list = Survey_Model.objects.all()
        survey_dictionary = {}
        survey_dictionary["surveys"]=[]
        for surv in survey_list:
            survey_dictionary["surveys"] += [{
                "id":surv.id,
                "survey":surv.survey_name,
                "creation":surv.survey_creation,
                "description":surv.survey_description,
                "size":surv.survey_size
            }]
        print(survey_dictionary)
        return JsonResponse(survey_dictionary)

@csrf_exempt
def event_api(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            #print(json_data['data'])
            eve = Event_Model(event=json_data['event'])
            eve.save()
            return HttpResponse("hello")
        except:
            return HttpResponse("Unexpected error:"+str(sys.exc_info()[0]))
    if request.method == "PUT":
        json_data = json.loads(request.body)
        try:
            eve = Event_Model.objects.get(pk=json_data['id'])
            eve.event = json_data['event']
            eve.save()

            #print(json_data['data'])
            return HttpResponse("hello")
        except:
            return HttpResponse("Unexpected error:"+str(sys.exc_info()[0]))
    if request.method == "DELETE":
        json_data = json.loads(request.body)
        try:
            eve = Event_Model.objects.get(pk=json_data['id'])
            eve.delete()
            #print(json_data['data'])
            return HttpResponse("hello")
        except:
            return HttpResponse("Unexpected error:"+str(sys.exc_info()[0]))
    if request.method == 'GET':
        event_list = Event_Model.objects.all()
        event_dictionary = {}
        event_dictionary["events"]=[]
        for eve in event_list:
            event_dictionary["events"] += [{
                "id":eve.id,
                "event":eve.name,
                "startdate":eve.start_date,
                "enddate":eve.end_date,
                "location":eve.location,
                "description":eve.description,
                "lng":eve.lng,
                "lat":eve.lat,
                "image":eve.image.path
            }]
        print(event_dictionary)
        return JsonResponse(event_dictionary)

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            #print(json_data['data'])
            ch = Chatline_Model(chat=json_data['chat'])
            ch.save()
            return HttpResponse("hello")
        except:
            return HttpResponse("Unexpected error:"+str(sys.exc_info()[0]))
    if request.method == "PUT":
        json_data = json.loads(request.body)
        try:
            ch = Chatline_Model.objects.get(pk=json_data['id'])
            ch.chat = json_data['chat']
            ch.save()

            #print(json_data['data'])
            return HttpResponse("hello")
        except:
            return HttpResponse("Unexpected error:"+str(sys.exc_info()[0]))
    if request.method == "DELETE":
        json_data = json.loads(request.body)
        try:
            ch = Chatline_Model.objects.get(pk=json_data['id'])
            ch.delete()
            #print(json_data['data'])
            return HttpResponse("hello")
        except:
            return HttpResponse("Unexpected error:"+str(sys.exc_info()[0]))
    if request.method == 'GET':
        chat_list = Chatline_Model.objects.all()
        chat_dictionary = {}
        chat_dictionary["chats"]=[]
        for ch in chat_list:
            chat_dictionary["chats"] += [{
                "id":ch.id,
                "chat":ch.chat.id,
                "user":ch.user.username,
                "creation":ch.creation,
                "text":ch.text,
            }]
        print(chat_dictionary)
        return JsonResponse(chat_dictionary)


# https://collingrady.wordpress.com/2008/02/18/editing-multiple-objects-in-django-with-newforms/
def register(request):
    if request.method == 'POST':
        rform = registration_form(request.POST)
        pform = profil_form(request.POST)
        if rform.is_valid() and pform.is_valid():
            new_user = rform.save(commit=True)
            new_profil = pform.save(commit=False)
            new_profil.user = new_user
            new_profil.save()
            return redirect("/")
    else:
        rform = registration_form()
        pform = profil_form()
    context = {
        "rform":rform,
        "pform":pform
    }
    return render(request,"registration/register.html",context)
