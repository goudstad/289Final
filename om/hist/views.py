from django.views.generic import DetailView, FormView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.urls import reverse_lazy
from .models import Decision, Employee #import data models
from .forms import fm_contact # import custom forms
from django.core.mail import send_mail

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

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_decisions = Decision.objects.all().count()
    # Decisions in progress
    num_decision_in_progress = Decision.objects.filter(decisionStatus__exact='1').count()
    # The 'all()' is implied by default.    
    num_employees = Employee.objects.count()
    context = {
        'num_decisions': num_decisions,
        'num_employees': num_employees,
        'num_decisions_in_progress': num_decision_in_progress
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'hist/index.html', context=context)

class ContactView(FormView):
    template_name = 'hist/contact.html'
    form_class = fm_contact

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        receiver = settings.CONTACT_EMAIL
        send_mail(subject, message, sender, [receiver])
        success = 'Message "{}" sent successfully'.format(message)
        context = {
            'form': fm_contact,
            'success': success
        }
        return render(self.request, 'hist/contact.html', context)