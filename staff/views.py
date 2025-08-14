from django.shortcuts import render, redirect, get_object_or_404
from .models import Staff
from .forms import StaffForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def add_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff:staff_list')
    else:
        form = StaffForm()
    return render(request, 'staff/add_staff.html', {'form': form})

# @login_required
def edit_staff(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method  == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff:staff_list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'staff/edit_staff.html', {'form': form, 'staff': staff})

# @login_required
def delete_staff(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('staff:staff_list')
    return render(request, 'staff/delete_staff.html', {'staff': staff})

# @login_required
def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'staff/staff_list.html', {'staff_members': staff_members})