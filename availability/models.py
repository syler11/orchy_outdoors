from django.db import models

# Create your models here.


class Availability(models.Model):
    """
    Request model class
    """  

    date = models.DateField(null=True, blank=False)
    podArate = models.CharField(max_length=10, null=False, blank=False, default="80")
    podAstatus = models.CharField(max_length=150, null=True, blank=False)
    podBrate = models.CharField(max_length=10, null=False, blank=False, default="80")
    podBstatus = models.CharField(max_length=150, null=True, blank=False)
    
    def __str__(self):
        """
        Returns Booking Number
        """
        return str(self.date)
