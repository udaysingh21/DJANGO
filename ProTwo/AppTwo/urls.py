from django.urls import path
from AppTwo import views

urlpatterns = [
    path('',views.index,name='index'),
    path('apptwo_help/',views.apptwo_help,name='apptwo_help'),

]