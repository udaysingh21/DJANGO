"""
URL configuration for level5 project.

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
from django.urls import path, include # import include function
from basic_app import views # import views.py from basic_app


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), # add index view to urlpatterns
    path('basic_app/', include('basic_app.urls')), # add basic_app/ to urlpatterns
    path('logout/', views.user_logout, name='logout'), # add logout view to urlpatterns
    path('special/', views.special, name='special'), # add special view to urlpatterns
]
