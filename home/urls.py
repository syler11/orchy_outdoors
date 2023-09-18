from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('booking/', views.booking, name='booking'),
    path('booking_details/(<selected_day>)/', views.booking_details, name='booking_details'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
]