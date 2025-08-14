from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name= 'attendance'

urlpatterns = [
    path('', login_required(views.AttendanceListView.as_view()), name='attendance_list'),
    path('add/', login_required(views.AttendanceCreateView.as_view()), name='attendance_add'),
    path('<int:pk>/', login_required(views.AttendanceDetailView.as_view()), name='attendance_detail'),
    path('<int:pk>/edit/', login_required(views.AttendanceUpdateView.as_view()), name='attendance_edit'),
    path('<int:pk>/delete/', login_required(views.AttendanceDeleteView.as_view()), name='attendance_delete'),
]