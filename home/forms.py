"""
Imports
"""
from django import forms
from .models import BookingPodA, BookingPodB


class AddBookingPodAForm(forms.ModelForm):
    """
    Add Booking form class
    """
    class Meta:
        """
        Meta info class
        """
        model = BookingPodA
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black w-75 rounded-0'


class AddBookingPodBForm(forms.ModelForm):
    """
    Add Booking form class
    """
    class Meta:
        """
        Meta info class
        """
        model = BookingPodB
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black w-75 rounded-0'