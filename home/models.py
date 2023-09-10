from django.db import models

# Create your models here.


class Booking(models.Model):
    """
    Request model class
    """  

    booking_id = models.CharField(max_length=10, null=True, blank=False)
    pod1 = models.CharField(max_length=20, null=True, blank=False)
    pod2 = models.CharField(max_length=20, null=True, blank=False)
    pod1_pax = models.IntegerField(null=True, blank=True)
    pod2_pax = models.IntegerField(null=True, blank=True)
    nights = models.IntegerField(null=True, blank=True)
    arrival_date = models.DateField(null=True, blank=False)
    pod1_rate = models.IntegerField(null=True, blank=True)
    pod2_rate = models.IntegerField(null=True, blank=True)
    total_cost = models.IntegerField(null=True, blank=False)
    fname = models.CharField(max_length=150, null=True, blank=False)
    lname = models.CharField(max_length=150, null=True, blank=False)
    phone_number = models.CharField(max_length=150, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    notes = models.CharField(max_length=150, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        """
        Returns Booking Number
        """
        return str(self.booking_id)
