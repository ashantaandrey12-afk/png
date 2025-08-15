from django import forms
from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        widgets = {
            'employment_date': forms.DateInput(attrs={'type': 'date'}),
        }