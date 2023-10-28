from django.urls import path, include
from . import views

urlpatterns = [
    path('faq/', views.faq, name='faq'),
    path('edit_faq/<int:id>/', views.edit_faq, name='edit_faq'),
    path('delete_faq/<int:id>/', views.delete_faq, name='delete_faq'),
]