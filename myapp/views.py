from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import *
from .forms import Survey_Form

from django.views.decorators.csrf import csrf_exempt

import json
import sys



# Create your views here.
def index(request):
    #return HttpResponse("CINS465 Hello World")
    return render(request, 'index.html', {"world_template":"CINS465 Hello World"})

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



def list(request, page_num):
    if page_num>=1:
        example_list=[]
        for i in range(page_num):
            example_list+=[i+1]

    else:
        example_list=None
    #return HttpResponse("Hello World")
    context={
        "page_template":page_num,
        "example_list":example_list
        }
    return render(request, 'list.html',context)
