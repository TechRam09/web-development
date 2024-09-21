from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to new app")

def registration(request):
    return HttpResponse("Welcome to new app registration")
