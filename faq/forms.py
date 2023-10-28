"""
Imports
"""
from django import forms
from .models import FAQ


class AddFAQForm(forms.ModelForm):
    """
    Add Booking form class
    """
    class Meta:
        """
        Meta info class
        """
        model = FAQ
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control border-info rounded-2'

class EditFAQForm(forms.ModelForm):
    """
    Add Availability form class
    """
    class Meta:
        """
        Meta info class
        """
        model = FAQ
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black w-75 rounded-0'