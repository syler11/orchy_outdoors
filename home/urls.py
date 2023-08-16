from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('booking/', views.booking, name='booking'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('local_info/', views.local_info, name='local_info'),
]