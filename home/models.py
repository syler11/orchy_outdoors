from django.db import models

# Create your models here.


class BookingPodA(models.Model):
    """
    Request model class
    """  

    booking_id = models.CharField(max_length=10, null=True, blank=False)
    podA = models.CharField(max_length=20, null=True, blank=False)
    pax = models.IntegerField(null=True, blank=True)
    nights = models.IntegerField(null=True, blank=True)
    arrival_date = models.DateField(null=True, blank=False)
    arrival_range = models.CharField(max_length=100, null=True, blank=False)
    podA_rate = models.IntegerField(null=True, blank=False)
    total_cost = models.IntegerField(null=True, blank=False)
    fname = models.CharField(max_length=150, null=True, blank=False)
    lname = models.CharField(max_length=150, null=True, blank=False)
    phone_number = models.CharField(max_length=150, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    notes = models.CharField(max_length=150, null=True, blank=True)
    status = models.CharField(max_length=150, null=True, blank=False, default="Available")
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    
    def __str__(self):
        """
        Returns Booking Number
        """
        return str(self.booking_id)


class BookingPodB(models.Model):
    """
    Request model class
    """  

    booking_id = models.CharField(max_length=10, null=True, blank=True)
    podB = models.CharField(max_length=20, null=True, blank=True)
    pax = models.IntegerField(null=True, blank=True)
    nights = models.IntegerField(null=True, blank=True)
    arrival_date = models.DateField(null=True, blank=False)
    arrival_range = models.CharField(max_length=100, null=True, blank=False)
    podB_rate = models.IntegerField(null=True, blank=True)
    total_cost = models.IntegerField(null=True, blank=True)
    fname = models.CharField(max_length=150, null=True, blank=True)
    lname = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    notes = models.CharField(max_length=150, null=True, blank=True)
    status = models.CharField(max_length=150, null=True, blank=True, default="Available")
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    
    def __str__(self):
        """
        Returns Booking Number
        """
        return str(self.booking_id)
