from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import IncidentReport

class IncidentListView(ListView):
    model = IncidentReport
    template_name = 'incidentReport/incidents_list.html'
    context_object_name = 'incidents'

class IncidentCreateView(CreateView):
    model = IncidentReport
    template_name = 'incidentReport/incident_form.html'
    fields = ['child', 'date', 'description', 'severity']
    success_url = reverse_lazy('incidentReport:incident_list')

class IncidentDetailView(DetailView):
    model = IncidentReport
    template_name = 'incidentReport/incident_detail.html'
    context_object_name = 'incident'

class IncidentUpdateView(UpdateView):
    model = IncidentReport
    template_name = 'incidentReport/incident_form.html'
    fields = ['child', 'date', 'description', 'severity']
    success_url = reverse_lazy('incidentReport:incident_list')

class IncidentDeleteView(DeleteView):
    model = IncidentReport
    template_name = 'incidentReport/incident_confirm_delete.html'
    success_url = reverse_lazy('incidentReport:incident_list')
