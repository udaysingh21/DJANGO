from django.shortcuts import render


# This is a Function Based View
# def index(request):
#     return render(request, 'index.html')

# This is Class Based View
# from django.views.generic import View,TemplateView
# from django.http import HttpResponse
#
# class CBView(View): # class CBView inherits from View class
#     def get(self,request):
#         return HttpResponse("Class Based View are Cool!")


# This is Template Based View
from django.views.generic import View,TemplateView

class IndexView(TemplateView):
    template_name='index.html'

    # argument in the form of dictionary
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['injectme']='BASIC INJECTION'
        return context
