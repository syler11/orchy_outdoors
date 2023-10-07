from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import AddAvailabilityForm
from orchy_outdoors.settings import BASE_RATE
from datetime import date, datetime
from .models import Availability

# Create your views here.
def availability(request):
    """ A view to return the availability page """
    

    today = date.today()

    restrictions = Availability.objects.filter(date__gte=today)

    if request.method == 'POST':
        form = AddAvailabilityForm(request.POST, request.FILES)
        if form.is_valid():
            availability = form.save()

            messages.success(request, 'Date restrictions was succesfully created!')
            return redirect(reverse('availability'))

        else:
            messages.error(request,
                        'Failed to create booking. \
                            Please ensure the form is valid.')
    else:
        form = AddAvailabilityForm()


    context = {
        'form': form,
        'BASE_RATE': BASE_RATE,
        'restrictions': restrictions
    }

    return render(request, 'availability/availability.html', context)

