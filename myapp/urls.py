from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('survey/',views.survey_view),
    path('list<int:page_num>/',views.list),
]
