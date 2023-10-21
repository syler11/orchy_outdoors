from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import AddAvailabilityForm, EditAvailabilityForm
from orchy_outdoors.settings import BASE_RATE
from datetime import date, datetime
from .models import Availability
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def availability(request):
    """ A view to return the availability page """
    
    messages.success(request, 'Date restrictions was succesfully created!')

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


@login_required
def edit_availability(request, id):
    """ A view to return the edit booking page """

    availability = get_object_or_404(Availability, pk=id)

    if request.method == 'POST':
        form = EditAvailabilityForm(request.POST, instance=availability)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {availability.id}!')
            return redirect(reverse('availability'))
        else:
            messages.error(request,
                           'Failed to update hours.\
                            Please ensure the form is valid.')
    else:
        form = EditAvailabilityForm(instance=availability)
        messages.info(request, f'You are editing {availability.id}')

    context = {
        'availability': availability,
        'form': form,
        }

    return render(request, 'availability/edit_availability.html', context)


@login_required
def delete_restriction(request, id):
    """
    Delete an employee from database
    """

    availability = get_object_or_404(Availability, pk=id)
    availability.delete()
    messages.success(request, 'Restriction deleted!')
    return redirect(reverse('availability'))