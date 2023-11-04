from django.contrib import admin
from .models import DateSettings


class DateSettingsAdmin(admin.ModelAdmin):
    """
    Payment admin model class
    """
    list_display = (
        'month_number',
        'full_date',
        'month_year',
        'is_display'
    )
    list_filter = (
        'month_number',
        'full_date',
        'month_year',
        'is_display'
    )
    search_fields = (
        'month_number',
        'full_date',
        'month_year',
        'is_display'
    )

    ordering = ('month_number',)


admin.site.register(DateSettings, DateSettingsAdmin)
