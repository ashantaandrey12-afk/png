# from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
# from .models import ParentGuardian
# from .forms import ParentGuardianForm
# from pa

# # Create your views here.
# def parent_list(request):
#     parents = ParentGuardian.objects.all()
#     return render(request, 'parent_list.html', {'parents': parents})

# def parent_create(request):
#     if request.method == 'POST':
#         form = ParentGuardianForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('parents:parent_list')
#     else:
#         form = ParentGuardianForm()
#     return render(request, 'parent_form.html', {'form': form})

# def parent_update(request, pk):
#     parent = get_object_or_404(ParentGuardian, pk=pk)
#     if request.method == 'POST':
#         form = ParentGuardianForm(request.POST, instance=parent)
#         if form.is_valid():
#             form.save()
#             return redirect('parents:parent_list')
#     else:
#         form = ParentGuardianForm(instance=parent)
#     return render(request, 'parent_form.html', {'form':form})

# def parent_delete(request, pk):
#     parent = get_object_or_404(ParentGuardian, pk=pk)
#     if request.method == 'POST':
#         parent.delete()
#         return redirect('parents:parent_list')
#     return render(request, 'parent_confirm_delete.html', {'parent':parent})

# class ParentDetailView(DetailView):
#     model= ParentGuardian
#     template_name = 'parent_detail.html'
#     context_object_name = 'parents'

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ParentGuardian

class ParentListView(ListView):
    model = ParentGuardian
    template_name = 'parents/parent_list.html'
    context_object_name = 'parents'

class ParentCreateView(CreateView):
    model = ParentGuardian
    template_name = 'parents/parent_form.html'
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'address', 'relationship_to_child']
    success_url = reverse_lazy('parents:parent_list')

class ParentDetailView(DetailView):
    model = ParentGuardian
    template_name = 'parents/parent_detail.html'
    context_object_name = 'parent'

class ParentUpdateView(UpdateView):
    model = ParentGuardian
    template_name = 'parents/parent_form.html'
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'address', 'relationship_to_child']
    success_url = reverse_lazy('parents:parent_list')

class ParentDeleteView(DeleteView):
    model = ParentGuardian
    template_name = 'parents/parent_confirm_delete.html'
    success_url = reverse_lazy('parents:parent_list')
