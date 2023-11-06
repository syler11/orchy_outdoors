"""
Imports
"""
from django import forms
from .models import DateSettings
from home.models import PageSettings


class AddDateSettingsForm(forms.ModelForm):
    """
    Add Booking form class
    """
    class Meta:
        """
        Meta info class
        """
        model = DateSettings
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black w-75 rounded-0'


class EditDateSettingsForm(forms.ModelForm):
    """
    Add Booking form class
    """
    class Meta:
        """
        Meta info class
        """
        model = DateSettings
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black w-75 rounded-0'


class EditPageSettingsForm(forms.ModelForm):
    """
    Add Booking form class
    """
    class Meta:
        """
        Meta info class
        """
        model = PageSettings
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black w-75 rounded-0'