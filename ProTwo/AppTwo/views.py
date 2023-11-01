from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("<em>my second project</em>")
    my_dict = {'insert_help': 'This is HELP calling from PROTWO APPTWO VIEWS.py'}
    return render(request,"apptwo/index.html",context=my_dict)

def apptwo_help(request):
    my_dict = {'insert_help': 'This is HELP calling from PROTWO APPTWO VIEWS.py'}
    return render(request,"apptwo/index.html",context=my_dict)
