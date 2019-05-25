from django.views.generic import DetailView, FormView, ListView, TemplateView
from django.shortcuts import render, get_object_or_404
from .models import Decision, Employee

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

class EmployeeList (ListView):
	model = Employee
	context_object_name = 'employee'

class EmployeeDetail(DetailView):
	model = Employee
	context_object_name = 'employee'
