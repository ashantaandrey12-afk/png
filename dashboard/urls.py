# dashboard/urls.py
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'dashboard'

urlpatterns = [
    path('', login_required(views.dashboard_home), name='dashboard_home'),
    path('children/', include('children.urls')),
    path('staff/', include('staff.urls')),
    path('attendance/', include('attendance.urls')),
    path('incidents/', include('incidentReport.urls')),
    path('classrooms/', include('classroom.urls')),
    path('schedule/', include('schedule.urls')),
    path('parents/', include('parents.urls')),
    path('settings/', views.settings_view, name='settings'),
]