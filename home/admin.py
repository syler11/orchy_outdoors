from django.forms import TextInput, Textarea
from django.db import models
from django.contrib import admin
from home.models import BookingPodA, BookingPodB, PageSettings, ContentSettings

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


class ContentSettingsAdmin(admin.ModelAdmin):
    """
    Payment admin model class
    """

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'60'})},
        models.TextField: {'widget': Textarea(attrs={'rows':10, 'cols':100})},
    }

    list_display = (
        'content_name',
        'content',
    )
    list_filter = (
        'content_name',
        'content',
    )
    search_fields = (
        'content_name',
        'content',
    )

    ordering = ('content_name',)


admin.site.register(BookingPodA, BookingPodAAdmin)
admin.site.register(BookingPodB, BookingPodBAdmin)
admin.site.register(PageSettings, PageSettingsAdmin)
admin.site.register(ContentSettings, ContentSettingsAdmin)
