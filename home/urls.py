from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home, name='home'),
    path('result',views.selection, name='result'),
    path('new',views.new, name='new'),
    path('hope',views.new, name='hope'),
]