from django import forms
from django.core import validators

'''
It is advised to use django built-in validators to verify django form field
'''

# def check_for_z(value):
#     if value[0].lower()!='z':
#         raise forms.ValidationError("Needs to start with z..")

class FormName(forms.Form):
    # name=forms.CharField(validators=[check_for_z])
    name=forms.CharField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label="Enter your email again:")
    text=forms.CharField(widget=forms.Textarea)

    # how to use hidden field , hidden from user , present in HTML
    # botcatcher=forms.CharField(required=False,
    #                            widget=forms.HiddenInput,
    #                            validators=[validators.MaxLengthValidator(0)])


    # def clean_botcatcher(self):
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("GOTCHA BOT..")
    #     return botcatcher

    # if you want to clean the entire form using Single method
    # super() is important
    # you can validate everything at once.
    def clean(self):
        all_clean_data=super(FormName, self).clean()
        email=all_clean_data['email']
        vmail=all_clean_data['verify_email']

        name=all_clean_data['name']
        if name[0]!='U':
            raise forms.ValidationError("Make sure Name starts with U")

        if email!=vmail:
            raise forms.ValidationError("Make sure Emails Match ...")