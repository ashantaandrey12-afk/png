from django.db import models

# Create your models here.
class ParentGuardian(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    address = models.TextField()
    relationship_to_child = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number} {self.email} {self.address} {self.relationship_to_child}"