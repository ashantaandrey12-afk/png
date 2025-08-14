from django.db import models
from children.models import Child
#Model for incident report
class IncidentReport(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date = models.DateField()
    staff_involved = models.ForeignKey('staff.Staff', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    action_taken = models.TextField()

    def __str__(self):
        return f"Incident Report for {self.child} on {self.date} {self.description} and {self.action_taken}"