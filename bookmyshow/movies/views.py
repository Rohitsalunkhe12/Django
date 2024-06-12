from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_movies(request):
    message = "<h1><marquee> Welcome to movies</marquee></h1>"
    return HttpResponse(message)
