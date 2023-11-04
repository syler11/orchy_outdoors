from django.db import models

# Create your models here.
class DateSettings(models.Model):
    """
    Request model class
    """  

    DISPLAY_CHOICES = [('Yes', "Yes"), ('No', "No")]

    month_number = models.CharField(max_length=200, null=True, blank=True)
    full_date = models.CharField(max_length=200, null=True, blank=True)
    month_year = models.CharField(max_length=20, null=True, blank=True)
    is_display = models.CharField(max_length=3, choices=DISPLAY_CHOICES, default="Yes")
    
    def __str__(self):
        """
        Returns Booking Number
        """
        return str(self.month_year)