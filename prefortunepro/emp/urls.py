from django.contrib import admin
from django.urls import path,include
from emp import views

urlpatterns = [
   path('',views.index),
]
