from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('faq/', views.faq, name = 'faq'),
    path('donor/', views.donor, name='donor'),
    path('patient/', views.patient, name='patient'),
    path('citizen/', views.citizen, name = 'citizen'),
    path('about/', views.about, name='about'),
    path('involve/', views.involve, name='involve')

]
