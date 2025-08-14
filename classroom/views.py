from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Classroom

class ClassroomListView(ListView):
    model = Classroom
    template_name = 'classroom/classroom_list.html'
    context_object_name = 'classrooms'

class ClassroomCreateView(CreateView):
    model = Classroom
    template_name = 'classroom/classroom_form.html'
    fields = ['name', 'capacity', 'teacher_in_charge']
    success_url = reverse_lazy('classroom:classroom_list')

class ClassroomDetailView(DetailView):
    model = Classroom
    template_name = 'classroom/classroom_detail.html'
    context_object_name = 'classroom'

class ClassroomUpdateView(UpdateView):
    model = Classroom
    template_name = 'classroom/classroom_form.html'
    fields = ['name', 'capacity', 'teacher_in_charge']
    success_url = reverse_lazy('classroom:classroom_list')

class ClassroomDeleteView(DeleteView):
    model = Classroom
    template_name = 'classroom/classroom_confirm_delete.html'
    success_url = reverse_lazy('classroom:classroom_list')
