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

# from django.urls import path
# from . import views
# from django.contrib.auth.decorators import login_required

# app_name = 'staff'  # Add this namespace
# urlpatterns = [
#     path('', login_required(views.StaffListView.as_view()), name='staff_list'),
#     path('add/', login_required(views.StaffCreateView.as_view()), name='staff_add'),
#     path('<int:pk>/', login_required(views.StaffDetailView.as_view()), name='staff_detail'),
#     path('<int:pk>/edit/', login_required(views.StaffUpdateView.as_view()), name='staff_edit'),
#     path('<int:pk>/delete/', login_required(views.StaffDeleteView.as_view()), name='staff_delete'),
# ]