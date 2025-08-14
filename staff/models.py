from django.db import models
#from children.models import Child

#Model for staff
class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='staff_photos/', null=True, blank=True)
    employment_date = models.DateField()
    specialty = models.CharField(max_length=100, blank=True)
    shift_hours = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.position} {self.email} {self.phone_number} {self.photo} {self.employment_date} {self.specialty} {self.shift_hours}"