from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import DateSettings
from .forms import AddDateSettingsForm,EditDateSettingsForm
from datetime import date, timedelta, datetime


# Create your views here.
def settings(request):
    """ A view to return the faq page """

    nowDate = datetime.now()
    this_year = int(nowDate.strftime("%Y"))
    year_two = this_year + 1
    year_three = this_year + 2
    
    dateset = DateSettings.objects.all()

    context = {
        'dateset': dateset,
        'this_year': this_year,
        'year_two': year_two,
        'year_three': year_three,
    }

    return render(request, 'settings/settings.html', context)


def add_month(request):

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