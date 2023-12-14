from djmoney.models.fields import MoneyField
from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class BookingPodA(models.Model):
    """
    Request model class
    """  
    class Meta:
        verbose_name_plural = "POD A"

    booking_id = models.CharField(max_length=10, null=True, blank=False)
    pod_name = models.CharField(max_length=20, null=True, blank=False)
    pax = models.IntegerField(null=True, blank=True)
    nights = models.IntegerField(null=True, blank=True)
    arrival_date = models.DateField(null=True, blank=False)
    arrival_range = models.CharField(max_length=100, null=True, blank=False)
    pod_rate = models.IntegerField(null=True, blank=False)
    total_cost = models.IntegerField(null=True, blank=False)
    fname = models.CharField(max_length=150, null=True, blank=False)
    lname = models.CharField(max_length=150, null=True, blank=False)
    phone_number = models.CharField(max_length=150, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    country = CountryField(
            blank_label='Country',
            null=True,
            blank=True
    )
    notes = models.CharField(max_length=150, null=True, blank=True)
    eta = models.CharField(max_length=150, null=True, blank=True)
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
    class Meta:
        verbose_name_plural = "POD B"

    booking_id = models.CharField(max_length=10, null=True, blank=True)
    pod_name = models.CharField(max_length=20, null=True, blank=True)
    pax = models.IntegerField(null=True, blank=True)
    nights = models.IntegerField(null=True, blank=True)
    arrival_date = models.DateField(null=True, blank=False)
    arrival_range = models.CharField(max_length=100, null=True, blank=False)
    pod_rate = models.IntegerField(null=True, blank=True)
    total_cost = models.IntegerField(null=True, blank=True)
    fname = models.CharField(max_length=150, null=True, blank=True)
    lname = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    country = CountryField(
            blank_label='Country',
            null=True,
            blank=True
    )
    notes = models.CharField(max_length=150, null=True, blank=True)
    eta = models.CharField(max_length=150, null=True, blank=True)
    status = models.CharField(max_length=150, null=True, blank=True, default="Available")
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    
    def __str__(self):
        """
        Returns Booking Number
        """
        return str(self.booking_id)


class PageSettings(models.Model):
    """
    Request model class
    """  
    class Meta:
        verbose_name_plural = "Page Settings"

    page_name = models.CharField(max_length=200, null=True, blank=True)
    page_url = models.CharField(max_length=200, null=True, blank=True)
    page_email = models.EmailField(null=True, blank=True)
    page_phone = models.CharField(max_length=150, null=True, blank=True)
    annual_rate = models.DecimalField(max_digits=6, default=0.00, decimal_places=2)
    
    def __str__(self):
        """
        Returns Booking Number
        """
        return str(self.page_name)


class ContentSettings(models.Model):
    """
    Request model class
    """  

    class Meta:
        verbose_name_plural = "Content"

    content_name = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(max_length=2000, null=True, blank=True)
    
    def __str__(self):
        """
        Returns Booking Number
        """
        return str(self.content_name)