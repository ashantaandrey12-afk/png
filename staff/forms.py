from django import forms
from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

    hire_date = forms.DateField(input_formats=['%Y-%m-%d'],widget=forms.DateInput(attrs={'type': 'date'}))