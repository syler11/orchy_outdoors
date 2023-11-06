from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import DateSettings
from .forms import AddDateSettingsForm,EditDateSettingsForm
from datetime import date, timedelta, datetime


# Create your views here.
@login_required
def settings(request):
    """ A view to return the faq page """

    nowDate = datetime.now()
    this_year = int(nowDate.strftime("%Y"))
    year_two = this_year + 1
    year_three = this_year + 2

    today = nowDate.strftime("%Y-%m-%d")
    
    dateset = DateSettings.objects.filter(full_date__gte=today).order_by('full_date')

    context = {
        'dateset': dateset,
        'this_year': this_year,
        'year_two': year_two,
        'year_three': year_three,
    }

    return render(request, 'settings/settings.html', context)

@login_required
def add_dateset(request):

    if request.method == 'POST':
        form = AddDateSettingsForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save()

           

            messages.success(request, 'Month was succesfully created!')
            return redirect(reverse('settings'))

        else:
            messages.error(request,
                           'Failed to add month. \
                            Please ensure the form is valid.')
    else:
        form = AddDateSettingsForm()

    context = {
        'form': form,
    }

    return render(request, 'settings/settings.html', context)


@login_required
def edit_dateset(request, id):


    dateset = get_object_or_404(DateSettings, pk=id)

    if request.method == 'POST':
        form = EditDateSettingsForm(request.POST, instance=dateset)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {dateset.month_year}!')
            return redirect(reverse('settings'))
        else:
            messages.error(request,
                           'Failed to update hours.\
                            Please ensure the form is valid.')
    else:
        form = EditDateSettingsForm(instance=dateset)
        messages.info(request, f'You are editing {dateset.month_year}')

    context = {
        'dateset': dateset,
        'form': form,
    }

    return render(request, 'settings/edit_dateset.html', context)


@login_required
def delete_dateset(request, id):
    """
    Delete a faq from database
    """

    dateset = get_object_or_404(DateSettings, pk=id)
    dateset.delete()
    messages.success(request, f'{dateset.month_year} was deleted!')
    return redirect(reverse('settings'))