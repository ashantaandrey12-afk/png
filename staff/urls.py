from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'staff'

urlpatterns = [
    path('', login_required(views.staff_list), name='staff_list'),
    path('add/', login_required(views.add_staff), name='add_staff'),
    path('edit/<int:pk>/', login_required(views.edit_staff), name='edit_staff'),
    path('delete/<int:pk>/', login_required(views.delete_staff), name='delete_staff'),
]