from django.contrib import admin
from faq.models import FAQ

# Register your models here.


class FAQAdmin(admin.ModelAdmin):
    """
    Payment admin model class
    """
    list_display = (
        'faq_choices',
        'sort_number',
        'title',
        'text',
    )
    list_filter = (
        'faq_choices',
        'sort_number',
        'title',
        'text',
    )
    search_fields = (
        'faq_choices',
        'sort_number',
        'title',
        'text',
    )

    ordering = ('sort_number',)

admin.site.register(FAQ, FAQAdmin)