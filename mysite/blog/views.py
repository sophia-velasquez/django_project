# from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

data = {

    "Name": "Sophia Velasquez",

    "Track": "Backend(Python)",

    "Message": "Hello there! 👋🏼"

}


def index(request):
    return JsonResponse(data)
