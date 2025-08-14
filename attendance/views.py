from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Attendance

class AttendanceListView(ListView):
    model = Attendance
    template_name = 'attendance/attendance_list.html'
    context_object_name = 'attendances'

class AttendanceCreateView(CreateView):
    model = Attendance
    template_name = 'attendance/attendance_form.html'
    fields = ['child', 'date', 'status']
    success_url = reverse_lazy('attendance:attendance_list')

class AttendanceDetailView(DetailView):
    model = Attendance
    template_name = 'attendance/attendance_detail.html'
    context_object_name = 'attendance'

class AttendanceUpdateView(UpdateView):
    model = Attendance
    template_name = 'attendance/attendance_form.html'
    fields = ['child', 'date', 'status']
    success_url = reverse_lazy('attendance:attendance_list')

class AttendanceDeleteView(DeleteView):
    model = Attendance
    template_name = 'attendance/attendance_confirm_delete.html'
    success_url = reverse_lazy('attendance:attendance_list')