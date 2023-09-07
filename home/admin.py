from django.contrib import admin
from .models import Booking

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    """
    Payment admin  model class
    """
    list_display = (
        'booking_id',
        'arrival_date',
        'pod1',
        'pod2',
        'lname',
        'total_cost',
    )
    list_filter = (
        'booking_id',
        'arrival_date',
        'pod1',
        'pod2',
        'lname',
        'total_cost',
    )
    search_fields = (
        'booking_id',
        'arrival_date',
        'pod1',
        'pod2',
        'lname',
        'total_cost',
    )

    ordering = ('arrival_date',)


admin.site.register(Booking, BookingAdmin)
