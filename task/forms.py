from .models import Days
from django import forms

class DaysForm(forms.ModelForm):
    class Meta:
        model = Days
        fields = '__all__'
