"""
URL configuration for learning_template project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include # include is used to include the urls of other apps
from basic_app import views

urlpatterns = [

    path('admin/', admin.site.urls),
    # if someone comes on domain page then it will say go to views , grab the index page and show it
    path('',views.index,name='index'),
    # if someone comes on domain.com/basic_app/here_anything like relative or other, then it will go to url file of basic_app and check if there is any url with anything
    # if there is any url with anything then it will go to views and grab the function and show it
    path('basic_app/',include('basic_app.urls')),
]
