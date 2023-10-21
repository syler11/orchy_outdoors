from django.contrib import admin
from home.models import BookingPodA, BookingPodB

# Register your models here.


class BookingPodAAdmin(admin.ModelAdmin):
    """
    Payment admin model class
    """
    list_display = (
        'booking_id',
        'arrival_date',
        'pod_name',
        'lname',
        'total_cost',
    )
    list_filter = (
        'booking_id',
        'arrival_date',
        'pod_name',
        'lname',
        'total_cost',
    )
    search_fields = (
        'booking_id',
        'arrival_date',
        'pod_name'
        'lname',
        'total_cost',
    )

    ordering = ('arrival_date',)

class BookingPodBAdmin(admin.ModelAdmin):
    """
    Payment admin model class
    """
    list_display = (
        'booking_id',
        'arrival_date',
        'pod_name',
        'lname',
        'total_cost',
    )
    list_filter = (
        'booking_id',
        'arrival_date',
        'pod_name',
        'lname',
        'total_cost',
    )
    search_fields = (
        'booking_id',
        'arrival_date',
        'pod_name'
        'lname',
        'total_cost',
    )

    ordering = ('arrival_date',)


admin.site.register(BookingPodA, BookingPodAAdmin)
admin.site.register(BookingPodB, BookingPodBAdmin)
