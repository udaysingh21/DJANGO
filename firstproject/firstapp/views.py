from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # Each view must return an HttpRespnse Object
    return HttpResponse("Hello World!!")


