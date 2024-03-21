from django.contrib import admin
from django.urls import path
from .views import show

urlpatterns = [
    path('', show, name='show')
]
