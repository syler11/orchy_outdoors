from django.urls import path, include
from . import views

urlpatterns = [
    path('reports/', views.reports, name='reports'),
]