from django.urls import path, include
from . import views

urlpatterns = [
    path('settings/', views.settings, name='settings'),
    #path('edit_settings/<int:id>/', views.edit_settings, name='edit_settings'),
    #path('delete_settings/<int:id>/', views.delete_settings, name='delete_settings'),
]