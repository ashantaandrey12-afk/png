from django.db import models
from children.models import Child

# Create your models here.

#Model for attendance
class Attendance(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Attendance for {self.child} on {self.date} is {self.status}"