from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Departments
from django.views.generic.list import ListView
from .forms import AddDepartment
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.


class ListDepartments(ListView):
    template_name = "departments/list_departments.html"
    model = Departments
    context_object_name = 'departments'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #filtered = Departments.objects.exclude(latitude=None)[:10]
        filtered = Departments.objects.filter(agency_name='test')
        #hello = Departments.objects.filter(state_name='Delaware').values('agency_name')[:20]
        context['departments'] = filtered
        #context['test'] = hello
        return context

class NewDepartment(CreateView):
    model = Departments
    template_name = "departments/add_department.html"
    fields = ['agency_name', 'state_name', 'latitude', 'longitude']
    success_url = '/crimes/'

class EditDepartment(UpdateView):
    model = Departments
    template_name = "departments/edit_department.html"
    success_url = '/crimes/'
    form_class = AddDepartment


# def get_queryset(self):
#         # queryset = super().get_queryset()
#         # self.kwargs == {'pk': 1}
#         # self.model = Cars
#         return self.model.objects.filter(**self.kwargs)