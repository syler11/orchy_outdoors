from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('booking/', views.booking, name='booking'),
    path('fof/', views.fof, name='fof'),
    path('booking_detailsPodA/(<selected_day>)/', views.booking_detailsPodA, name='booking_detailsPodA'),
    path('booking_detailsPodB/(<selected_day>)/', views.booking_detailsPodB, name='booking_detailsPodB'),
    path('booking_savePodA/', views.booking_savePodA, name='booking_savePodA'),
    path('booking_savePodB/', views.booking_savePodB, name='booking_savePodB'),
    path('booking_successPodA/<int:id>', views.booking_successPodA, name='booking_successPodA'),
    path('booking_successPodB/<int:id>', views.booking_successPodB, name='booking_successPodB'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('planner/', views.planner, name='planner'),
    path('reservation_details/<booking_id>', views.reservation_details, name='reservation_details'),
    path('all_reservations/', views.all_reservations, name='all_reservations'),
]