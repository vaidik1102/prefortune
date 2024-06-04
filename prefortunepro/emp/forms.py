from django import forms
from .models import employee

class emp_reg(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'
        