from django.shortcuts import render, redirect, reverse, get_object_or_404
from faq.models import FAQ
from .forms import AddFAQForm, EditFAQForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def faq(request):
    """ A view to return the faq page """

    faq = FAQ.objects.all().order_by("sort_number")

    accomodation_count = FAQ.objects.filter(faq_choices="ACCOMODATION").count()+1
    amenities_count = FAQ.objects.filter(faq_choices="AMENITIES").count()+1
    miscellanous_count = FAQ.objects.filter(faq_choices="MISCELLANOUS").count()+1

    if request.method == 'POST':
        form = AddFAQForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save()

            messages.success(request, 'New FAQ was succesfully created!')
            return redirect(reverse('faq'))

        else:
            messages.error(request,
                           'Failed to create FAQ. \
                            Please ensure the form is valid.')

    else:
        form = AddFAQForm()

    context = {
        'faq': faq,
        'accomodation_count': accomodation_count,
        'amenities_count': amenities_count,
        'miscellanous_count': miscellanous_count,
        'form': form,
    }

    return render(request, 'faq/faq.html', context)


@login_required
def edit_faq(request, id):


    faq = get_object_or_404(FAQ, pk=id)

    if request.method == 'POST':
        form = EditFAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {faq.title}!')
            return redirect(reverse('faq'))
        else:
            messages.error(request,
                           'Failed to update hours.\
                            Please ensure the form is valid.')
    else:
        form = EditFAQForm(instance=faq)
        messages.info(request, f'You are editing {faq.title}')

    context = {
        'faq': faq,
        'form': form,
    }

    return render(request, 'faq/edit_faq.html', context)


@login_required
def delete_faq(request, id):
    """
    Delete a faq from database
    """

    faq = get_object_or_404(FAQ, pk=id)
    faq.delete()
    messages.success(request, f'FAQ - {faq.title} was deleted!')
    return redirect(reverse('faq'))