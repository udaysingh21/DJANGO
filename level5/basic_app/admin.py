from django.contrib import admin
from basic_app.models import UserProfileInfo # import UserProfileInfo model from basic_app/models.py


# Register your models here.

admin.site.register(UserProfileInfo) # register UserProfileInfo model with admin site