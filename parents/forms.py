from django import forms
from .models import ParentGuardian

class ParentGuardianForm(forms.ModelForm):
    class Meta:
        model = ParentGuardian
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address', 'relationship_to_child']