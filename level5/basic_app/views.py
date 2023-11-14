from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm # import UserForm and UserProfileInfoForm from basic_app/forms.py

from django.contrib.auth import authenticate, login, logout # import authenticate, login, logout from django.contrib.auth
from django.http import HttpResponseRedirect, HttpResponse # import HttpResponseRedirect, HttpResponse from django.http
from django.urls import reverse # import reverse from django.urls
from django.contrib.auth.decorators import login_required # import login_required from django.contrib.auth.decorators




# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html') # render index.html template

def register(request):
    registered = False # set registered to False
    if request.method== 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid(): # check if both forms are valid
            user = user_form.save() # save user_form
            user.set_password(user.password) # hash password
            user.save() # save user

            profile = profile_form.save(commit=False) # save profile_form
            profile.user = user # set profile.user to user
            if 'profile_pic' in request.FILES: # check if profile_pic is in request.FILES
                profile.profile_pic = request.FILES['profile_pic'] # set profile.profile_pic to request.FILES['profile_pic']
            profile.save() # save profile

            registered = True # set registered to True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        # if request is not POST, create empty forms
        # this will be executed when user visits the register page for the first time
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered}) # render registration.html template


def user_login(request):

    if request.method=='POST':
        username=request.POST.get('username') # get username from request.POST
        password=request.POST.get('password') # get password from request.POST

        # this is where we authenticate the user automatically
        user = authenticate(username=username, password=password) # authenticate user

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index')) # redirect to index view
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request,'basic_app/login.html',{})

@login_required # use login_required decorator
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index')) # redirect to index view

@login_required # use login_required decorator
def special(request):
    return HttpResponse("You are logged in, Nice!")

