from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Topic,AccessRecord,Webpage


# Create your views here.

def index(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records': webpages_list}

    my_dict = {'insert_me': "Hello i am coming from firstapp's views.py"}
    return render(request,'firstapp/index.html',context=date_dict)

