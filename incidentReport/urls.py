from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'incidentReport'  # Add this namespace
urlpatterns = [
    path('', login_required(views.IncidentListView.as_view()), name='incident_list'),
    path('add/', login_required(views.IncidentCreateView.as_view()), name='incident_add'),
    path('<int:pk>/', login_required(views.IncidentDetailView.as_view()), name='incident_detail'),
    path('<int:pk>/edit/', login_required(views.IncidentUpdateView.as_view()), name='incident_edit'),
    path('<int:pk>/delete/', login_required(views.IncidentDeleteView.as_view()), name='incident_delete'),
]