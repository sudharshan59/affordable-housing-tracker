from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'contact', 'income']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'income': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }