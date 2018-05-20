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
    return render(request, 'index.html', {"world_template":"Ticket465"})

def map(request):
    if request.method == 'POST':
        form = Event_Form(request.POST)
        lng = request.POST.get('lng', None)
        lat = request.POST.get('lat', None)
        if form.is_valid():
            event = Event_Model(
                name=form.cleaned_data['name'],
                start_date=form.cleaned_data['start_date'],
                end_date=form.cleaned_data['end_date'],
                location=form.cleaned_data['location'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data['image'],
                lng=lng,
                lat=lat
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
        message = request.POST.get('msgfield', None)
        current_user = request.user
        current_user_id = request.user.id
        chat = Chatline_Model(
            user=current_user,
            text=message
        )
        chat.save()

    else:
        current_user_id = request.user.id

    context = {
        "current_user_id":current_user_id,
        }
    return render(request, 'chat.html', context)

def event(request):
    if request.method == 'POST':
        if 'Ticket' in request.POST:
            ticket_form = Ticket_Form(request.POST)
            if ticket_form.is_valid():
                ticket = Ticket_Model(
                    event=ticket_form.cleaned_data['event'],
                    price=ticket_form.cleaned_data['price'],
                    info=ticket_form.cleaned_data['info'],
                    user=request.user
                )
                ticket.save()
                ticket_form = Ticket_Form()
                bid_form = Bid_Form()
        elif 'Bid' in request.POST:
            bid_form = Bid_Form(request.POST)
            if bid_form.is_valid():
                value = bid_form.cleaned_data['ticket'].id
                bid = Ticket_Model(
                    id=int(value),
                    event=Ticket_Model.objects.get(id=value).event,
                    price=bid_form.cleaned_data['bid'],
                    bidder=request.user
                )
                bid.save(update_fields=['price','bidder'])
                bid_form = Bid_Form()
                ticket_form = Ticket_Form()
    else:
        ticket_form = Ticket_Form()
        bid_form = Bid_Form()

    ticket_list = Ticket_Model.objects.all()

    context = {
        "ticket_list":ticket_list,
        "ticket_form":ticket_form,
        "bid_form":bid_form
        }
    return render(request, 'event.html', context)

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
                #"image":eve.image.path
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
                "user":ch.user.username,
                "creation":ch.creation.strftime("%H:%M:%S - %Y/%m/%d"),
                "text":ch.text,
            }]
        print(chat_dictionary)
        return JsonResponse(chat_dictionary)


@csrf_exempt
def ticket_api(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            #print(json_data['data'])
            tick = Ticket_Model(ticket=json_data['ticket'])
            tick.save()
            return HttpResponse("hello")
        except:
            return HttpResponse("Unexpected error:"+str(sys.exc_info()[0]))
    if request.method == "PUT":
        json_data = json.loads(request.body)
        try:
            tick = Ticket_Model.objects.get(pk=json_data['id'])
            tick.ticket = json_data['ticket']
            tick.save()

            #print(json_data['data'])
            return HttpResponse("hello")
        except:
            return HttpResponse("Unexpected error:"+str(sys.exc_info()[0]))
    if request.method == "DELETE":
        json_data = json.loads(request.body)
        try:
            tick = Ticket_Model.objects.get(pk=json_data['id'])
            tick.delete()
            #print(json_data['data'])
            return HttpResponse("hello")
        except:
            return HttpResponse("Unexpected error:"+str(sys.exc_info()[0]))
    if request.method == 'GET':
        ticket_list = Ticket_Model.objects.all()
        ticket_dictionary = {}
        ticket_dictionary["tickets"]=[]
        for tick in ticket_list:
            if tick.bidder is not None:
                bidder = tick.bidder.username
            else:
                bidder = "None"
            ticket_dictionary["tickets"] += [{
                "id":tick.id,
                "user":tick.user.username,
                "bidder":bidder,
                "event":tick.event.name,
                "price":tick.price,
                "info":tick.info
            }]
        print(ticket_dictionary)
        return JsonResponse(ticket_dictionary)


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
