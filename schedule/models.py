from django.db import models

# Create your models here.
#Model for Schedule
class Schedule(models.Model):
    child = models.ForeignKey('children.Child', on_delete=models.CASCADE)
    date = models.DateTimeField()
    activity_name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.activity_name} for {self.child} from {self.start_time} to {self.end_time} given on {self.date}"