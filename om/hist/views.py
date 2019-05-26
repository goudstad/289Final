from django.views.generic import DetailView, FormView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.urls import reverse_lazy
from .models import Decision, Employee #import data models
from .forms import fm_addEmployee # import custom forms

# using functional view
#def decision_details(request, dec_id):
#    dec=get_object_or_404(Decision, pk=dec_id)
#    return render(request,'hist/decision_detail.html', {'decision': dec})

class DecisionList(ListView):
    model = Decision
    context_object_name = 'decision' # alias

class DecisionDetail(DetailView):
    model = Decision
    context_object_name = 'decision'

class DecisionCreate(CreateView):
    model = Decision
    fields= '__all__'

class DecisionUpdate(UpdateView):
    model = Decision
    fields= '__all__'

class DecisionDelete(DeleteView):
    model = Decision
    success_url = reverse_lazy('decision-list')

class EmployeeList (ListView):
    model = Employee
    context_object_name = 'employee'

class EmployeeDetail(DetailView):
    model = Employee
    context_object_name = 'employee'

class EmployeeCreate(CreateView):
    model = Employee
    fields= '__all__'

class EmployeeUpdate(UpdateView):
    model = Employee
    fields= '__all__'

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee-list')
