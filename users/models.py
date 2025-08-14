from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UserProfile(AbstractUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('Admin', 'Admin'), ('Staff', 'Staff'), ('Parent', 'Parent')])
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    def __str__(self):
        return f"{self.user.username} - {self.role}"

    class Meta:
        db_table="users"