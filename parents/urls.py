from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'parents'

urlpatterns = [
    path('', login_required(views.ParentListView.as_view()), name='parent_list'),
    path('create/', login_required(views.ParentCreateView.as_view()), name='parent_create'),
    path('<int:pk>/', login_required(views.ParentDetailView.as_view()), name='parent_detail'),
    path('<int:pk>/edit/', login_required(views.ParentUpdateView.as_view()), name='parent_update'),
    path('<int:pk>/delete/', login_required(views.ParentDeleteView.as_view()), name='parent_delete'),
]
