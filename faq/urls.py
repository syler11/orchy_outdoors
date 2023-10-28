from django.urls import path, include
from . import views

urlpatterns = [
    path('faq/', views.faq, name='faq'),
    #path('edit_availability/<int:id>/', views.edit_availability, name='edit_availability'),
    path('delete_faq/<int:id>/', views.delete_faq, name='delete_faq'),
]