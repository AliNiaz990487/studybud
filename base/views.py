from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Home Page")

def room(request):
    return HttpResponse("ROOM")