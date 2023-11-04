from django.urls import path, include
from . import views

urlpatterns = [
    path('settings/', views.settings, name='settings'),
    path('add_dateset/', views.add_dateset, name='add_dateset'),
    path('edit_dateset/<int:id>/', views.edit_dateset, name='edit_dateset'),
    #path('edit_settings/<int:id>/', views.edit_settings, name='edit_settings'),
    #path('delete_settings/<int:id>/', views.delete_settings, name='delete_settings'),
]