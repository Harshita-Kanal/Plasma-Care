from django.forms import ModelForm
from django import forms
from .models import Volunteer, RegisterDonor

class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'phone', 'email', 'description']


class DonorForm(ModelForm):
    class Meta:
        model = RegisterDonor
        fields = '__all__'
        
