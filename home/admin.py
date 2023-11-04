from django.contrib import admin
from home.models import BookingPodA, BookingPodB, PageSettings

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


class PageSettingsAdmin(admin.ModelAdmin):
    """
    Payment admin model class
    """
    list_display = (
        'page_name',
        'page_url',
        'page_email',
        'page_phone',
    )
    list_filter = (
        'page_name',
        'page_url',
        'page_email',
        'page_phone',
    )
    search_fields = (
        'page_name',
        'page_url',
        'page_email',
        'page_phone',
    )

    ordering = ('page_name',)


admin.site.register(BookingPodA, BookingPodAAdmin)
admin.site.register(BookingPodB, BookingPodBAdmin)
admin.site.register(PageSettings, PageSettingsAdmin)
