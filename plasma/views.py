from django.shortcuts import render
from . models import *
from .forms import VolunteerForm, DonorForm
from django.http import HttpResponseRedirect
def home(request):
    return render(request, 'plasma/main.html')


def faq(request):
    return render(request, 'plasma/faq.html')


def donor(request):
    form = DonorForm()
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            form = DonorForm()
    return render(request, 'plasma/donor.html', {'form' : form})


def patient(request):
    donors = RegisterDonor.objects.all()
    return render(request, 'plasma/patient.html', {'donors': donors})


def about(request):
    return render(request, 'plasma/About.html')


def involve(request):
    form = VolunteerForm()
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            form = VolunteerForm()
    return render(request, 'plasma/involve.html', {'form' : form})


def citizen(request):
    
    volunteer = Volunteer.objects.all()
    return render(request, 'plasma/citizen.html', {'volunteer': volunteer})

# Create your views here.
