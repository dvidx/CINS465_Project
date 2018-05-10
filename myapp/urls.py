from django.urls import path, include

from . import views
from .forms import LoginForm
from django.contrib.auth import views as adminviews

urlpatterns = [
    path('',views.index),
    path('surveys/',views.survey_api),
    path('map/',views.map),
    path('chat/',views.chat),
    path('chats/',views.chat_api),
    path('event/',views.event),
    path('events/',views.event_api),
    path('login/', adminviews.login, {
        'template_name':'registration/login.html',
        'authentication_form':LoginForm
    }, name="login"),
    path('logout/', adminviews.logout,{
        'next_page':'/login/'
    }),
    path('register/', views.register),
]
