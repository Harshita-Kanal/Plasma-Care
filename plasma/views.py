from django.shortcuts import render
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
    return render(request, 'plasma/citizen.html')
# Create your views here.
