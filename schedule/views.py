from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Schedule

class ScheduleListView(ListView):
    model = Schedule
    template_name = 'schedule/schedule_list.html'
    context_object_name = 'schedules'

class ScheduleCreateView(CreateView):
    model = Schedule
    template_name = 'schedule/schedule_form.html'
    fields = ['classroom', 'date', 'time', 'activity']
    success_url = reverse_lazy('schedule:schedule_list')

class ScheduleDetailView(DetailView):
    model = Schedule
    template_name = 'schedule/schedule_detail.html'
    context_object_name = 'schedule'

class ScheduleUpdateView(UpdateView):
    model = Schedule
    template_name = 'schedule/schedule_form.html'
    fields = ['classroom', 'date', 'time', 'activity']
    success_url = reverse_lazy('schedule:schedule_list')

class ScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = 'schedule/schedule_confirm_delete.html'
    success_url = reverse_lazy('schedule:schedule_list')