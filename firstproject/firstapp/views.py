from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # # Each view must return an HttpRespnse Object
    # return HttpResponse("Hello World!!")

    my_dict = {'insert_me': "Hello i am coming from firstapp's views.py"}
    return render(request,'firstapp/index.html',context=my_dict)

