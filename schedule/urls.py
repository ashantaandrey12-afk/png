from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'schedule'  # Add this namespace
urlpatterns = [
    path('', login_required(views.ScheduleListView.as_view()), name='schedule_list'),
    path('add/', login_required(views.ScheduleCreateView.as_view()), name='schedule_add'),
    path('<int:pk>/', login_required(views.ScheduleDetailView.as_view()), name='schedule_detail'),
    path('<int:pk>/edit/', login_required(views.ScheduleUpdateView.as_view()), name='schedule_edit'),
    path('<int:pk>/delete/', login_required(views.ScheduleDeleteView.as_view()), name='schedule_delete'),
]