from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'classroom'  # Add this namespace
urlpatterns = [
    path('', login_required(views.ClassroomListView.as_view()), name='classroom_list'),
    path('add/', login_required(views.ClassroomCreateView.as_view()), name='classroom_add'),
    path('<int:pk>/', login_required(views.ClassroomDetailView.as_view()), name='classroom_detail'),
    path('<int:pk>/edit/', login_required(views.ClassroomUpdateView.as_view()), name='classroom_edit'),
    path('<int:pk>/delete/', login_required(views.ClassroomDeleteView.as_view()), name='classroom_delete'),
]