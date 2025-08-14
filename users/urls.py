from django.urls import path
from . import views

app_name = 'users'

urlpatterns= [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
#     path('login/', views.login_user, name='login'),
#     path('logout/', views.logout_user, name='logout'),
#     path('register/', views.register_user, name='register'),
#     path('profile/', views.user_profile, name='user_profile'),
#     path('password_change/', views.change_password, name='change_password'),
#     path('password_reset/', views.reset_password, name='reset_password'),
#     path('password_reset_done/', views.password_reset_done, name='password_reset_done'),
#     path('password_reset_confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
#     path('password_reset_complete/', views.password_reset_complete, name='password_reset_complete'),
]