from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/home.html')

def booking(request):
    """ A view to return the booking page """

    return render(request, 'home/booking.html')


def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')

def local_info(request):
    """ A view to return the local_info page """

    return render(request, 'home/local_info.html')

def faq(request):
    """ A view to return the faq page """

    return render(request, 'home/faq.html')

def contact(request):
    """ A view to return the contact page """

    return render(request, 'home/contact.html')