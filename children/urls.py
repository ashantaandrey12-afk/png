from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'children'

urlpatterns = [
    path('', login_required(views.child_list), name='child_list'),
    path('add/', login_required(views.add_child), name='add_child'),
    path('edit/<int:pk>/', login_required(views.edit_child), name='edit_child'),
    path('delete/<int:pk>/', login_required(views.delete_child), name='delete_child'),
    path('profile/<int:pk>/', login_required(views.child_profile), name='child_profile'),
]