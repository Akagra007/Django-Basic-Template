from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from loginapp import views

urlpatterns = [
    path('',views.contact,name='contact'),
]
