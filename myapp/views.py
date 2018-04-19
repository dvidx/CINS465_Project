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
    return render(request, 'chat.html')

def event(request):
    return render(request, 'event.html')

def survey_view(request):
    if request.method == 'POST':
        form = Survey_Form(request.POST)
        if form.is_valid():
            surv = Survey_Model(
                survey_name=form.cleaned_data['survey_name'],
                survey_creation=form.cleaned_data['survey_creation'],
                survey_size=form.cleaned_data['survey_size'],
                survey_description=form.cleaned_data['survey_description']
            )
            surv.save()
            form = Survey_Form()
    else:
        form = Survey_Form()

    survey_list = Survey_Model.objects.all()
    context = {
        "survey_list":survey_list,
        "form":form
        }
    return render(request, 'survey.html', context)

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

def register(request):
    if request.method == 'POST':
        form = registration_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/")
    else:
        form = registration_form()
    context = {"form":form}
    return render(request,"registration/register.html",context)
