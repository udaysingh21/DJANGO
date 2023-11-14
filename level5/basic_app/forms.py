from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo  # import UserProfileInfo model from basic_app/models.py

# create a form class which inherits from forms.ModelForm
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput()) # password field will be hidden

    class Meta:
        model = User
        fields = ('username', 'email', 'password') # fields to be displayed in the form

# create a form class which inherits from forms.ModelForm
class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic') # fields to be displayed in the form

