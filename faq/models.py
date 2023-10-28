from django.db import models

# Create your models here.


class FAQ(models.Model):
    """
    Request model class
    """  

    FAQ_CHOICES = (
    ("ACCOMODATION", "Accomodation"),
    ("AMENITIES", "Amentities"),
    ("MISCELLANOUS", "Miscellanous"),
    )

    faq_choices = models.CharField(max_length=20,
                  choices=FAQ_CHOICES,
                  default="ACCOMODATION")
    sort_number = models.IntegerField(null=False, blank=False)
    title = models.CharField(max_length=150, null=True, blank=False)
    text = models.CharField(max_length=150, null=True, blank=False)
    
    def __str__(self):
        """
        Returns Sort Number
        """
        return str(self.sort_number)