from django.shortcuts import render
from project.models import User

# Create your views here.

def index(request):
    return render(request,'project/index.html')


def users(request):
    user_list=User.objects.order_by('first_name')
    user_dict={'users':user_list}
    return render(request,'project/user.html',context=user_dict)