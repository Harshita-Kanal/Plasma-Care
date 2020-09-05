from django.shortcuts import render
def home(request):
    return render(request, 'plasma/main.html')
# Create your views here.
