from django.db import models
from staff.models import Staff

# Create your models here.
#Model for Classroom
class Classroom(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField()
    children = models.ManyToManyField('children.Child', related_name='classrooms')

    def __str__(self):
        return f"{self.name} {self.teacher} {self.capacity} {self.children}"