from django.shortcuts import get_object_or_404
from .models import PageSettings


def page_settings(request):

    page_set = get_object_or_404(PageSettings, pk=1)
    print(page_set)


    context = {
        'page_set': page_set,
    }

    return context