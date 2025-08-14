from django.urls import path
from . import views

app_name = 'children'

urlpatterns = [
    path('', views.child_list,name='child_list'),
    path('add/', views.add_child, name='add_child'),
    path('edit/<int:pk>/', views.edit_child, name='edit_child'),
    path('delete/<int:pk>/', views.delete_child, name='delete_child'),
    path('profile/<int:pk>/', views.child_profile, name='child_profile'),
]