from django.shortcuts import render
from django.http import HttpResponse

from .models import Survey_Model
from .forms import Survey_Form

from django.views.decorators.csrf import csrf_exempt

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
                survey_size=form.cleaned_data['survey_size']
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
