from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def settings(request):
    """ A view to return the faq page """

   

    return render(request, 'settings/settings.html')