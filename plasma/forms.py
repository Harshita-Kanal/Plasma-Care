from django.forms import ModelForm
from .models import Volunteer

class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'phone', 'email', 'description']
        
