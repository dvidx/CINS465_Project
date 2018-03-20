from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('survey/',views.survey_view),
    path('surveys/',views.survey_api),
    path('list<int:page_num>/',views.list),
]
