from django.contrib import admin
from availability.models import Availability

# Register your models here.


class AvailabilityAdmin(admin.ModelAdmin):
    """
    Payment admin model class
    """
    list_display = (
        'date',
        'podArate',
        'podBrate',
        'podAstatus',
        'podBstatus',
    )
    list_filter = (
        'date',
        'podArate',
        'podBrate',
        'podAstatus',
        'podBstatus',
    )
    search_fields = (
        'date',
        'podArate',
        'podBrate',
        'podAstatus',
        'podBstatus',
    )

    ordering = ('date',)

admin.site.register(Availability, AvailabilityAdmin)
