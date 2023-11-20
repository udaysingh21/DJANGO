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

from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from basic_app import models
from django.urls import reverse_lazy

class SchoolListView(ListView):
    context_object_name='schools'
    model=models.School
    # by default the template name is school_list.html
    # you will be provided a list with every record in the School model

class SchoolDetailView(DetailView):
    context_object_name='school_detail'
    model=models.School
    template_name='basic_app/school_detail.html'
    # you will be provided a list with every record in the School model
    # the default context name is school

class SchoolCreateView(CreateView):
    fields=('name','principal','location')
    model=models.School
    success_url = reverse_lazy('basic_app:schools')

class SchoolUpdateView(UpdateView):
    fields=('name','principal')
    model=models.School
    success_url=  reverse_lazy('basic_app:schools')

class SchoolDeleteView(DeleteView):
    model=models.School
    success_url=reverse_lazy('basic_app:schools')

