from django.urls import path, include
from . import views

urlpatterns = [
    path('faq/', views.faq, name='faq'),
    #path('edit_availability/<int:id>/', views.edit_availability, name='edit_availability'),
    #path('delete_restriction/<int:id>/', views.delete_restriction, name='delete_restriction'),
]