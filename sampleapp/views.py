from django.shortcuts import render, HttpResponse


# Create your views here.
def abcd(request):
    return HttpResponse("Ha ha ha 555 ")

def ClentSample(request):
    return HttpResponse("Client")