from django import forms
from django.db.models import fields
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('name', 'mobile', 'age')