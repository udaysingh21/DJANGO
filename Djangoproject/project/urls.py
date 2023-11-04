from django.urls import path
from project import views


urlpatterns=[

    path('',views.users,name="users")
]