from django.shortcuts import render
from faq.models import FAQ

# Create your views here.
def faq(request):
    """ A view to return the faq page """

    faq = FAQ.objects.all().order_by("sort_number")

    context = {
        'faq': faq,
    }

    return render(request, 'faq/faq.html', context)