# dashboard/urls.py
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'dashboard'  # Define the namespace for the dashboard

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('children/', include('children.urls', namespace='children')),  # Include with namespace
    path('staff/', include('staff.urls', namespace='staff')),  # Include with namespace
    path('attendance/', include('attendance.urls', namespace='attendance')),  # Include with namespace
    path('incidents/', include('incidentReport.urls', namespace='incidentReport')),  # Include with namespace
    path('classrooms/', include('classroom.urls', namespace='classroom')),  # Include with namespace
    path('schedule/', include('schedule.urls', namespace='schedule')),  # Include with namespace
    path('parents/', include('parents.urls', namespace='parents')),  # Include with namespace
    path('settings/', views.settings_view, name='settings'),
]
