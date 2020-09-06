from django.shortcuts import render
from . models import *
from .forms import VolunteerForm
from django.http import HttpResponseRedirect
def home(request):
    return render(request, 'plasma/main.html')


def faq(request):
    return render(request, 'plasma/faq.html')


def donor(request):
    return render(request, 'plasma/donor.html')


def patient(request):
    return render(request, 'plasma/patient.html')


def about(request):
    return render(request, 'plasma/About.html')


def citizen(request):
    form = VolunteerForm()
    volunteer = Volunteer.objects.all()
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            form = VolunteerForm()
    return render(request, 'plasma/citizen.html', {'volunteer': volunteer, 'form': form})

# Create your views here.
