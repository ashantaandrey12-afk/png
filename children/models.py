from django.db import models
from datetime import date, datetime
#from staff.models import Staff
#from parents.models import ParentGuardian

# Create your models here.

#Model for a child
class Child (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=False, default=date(2005, 1, 1))
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], null=True, blank=False)
    parent_guardian = models.ForeignKey('parents.ParentGuardian', on_delete=models.CASCADE, related_name='children', null=True, blank=False)
    #parent_guardian = models.ManyToOne('parents.ParentGuardian', related_name='children')
    photo = models.ImageField(upload_to='child_photos/', null=True, blank=True)
    medical_info = models.TextField(blank=True)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.date_of_birth} {self.gender} {self.parent_guardian} {self.photo} {self.medical_info} {self.enrollment_date} {self.notes}"