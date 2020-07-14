from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results),
    path('<int:question_id>/votes/', views.votes),    #RESTful 방식
]
