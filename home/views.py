from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from orchy_outdoors.settings import DEFAULT_FROM_EMAIL
from home.models import BookingPodA, BookingPodB
from .forms import AddBookingPodAForm, AddBookingPodBForm
from availability.models import Availability

from datetime import date, timedelta, datetime

import uuid

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/home.html')


def booking(request):
    """ A view to return the booking page """

    nowDate = date.today()
    today = nowDate.strftime("%Y-%m-%d")
    print(today)

    if 'month-selector' in request.GET:
        firstDate = request.GET['month-selector']
        print(firstDate)
    else:
        firstDate = today

    bookPodA = BookingPodA.objects.filter(status="Booked")
    podA = list(bookPodA.values_list('arrival_range', flat=True))

    bookPodB = BookingPodB.objects.filter(status="Booked")
    podB = list(bookPodB.values_list('arrival_range', flat=True))

    restrictPodA = Availability.objects.filter(podAstatus="closed")
    restrPodA = list(restrictPodA.values_list('date', flat=True))

    restrictPodB = Availability.objects.filter(podBstatus="closed")
    restrPodB = list(restrictPodB.values_list('date', flat=True))

    parseDate = datetime.strptime(firstDate[0:8], "%Y-%m-")

    date1 = datetime.strptime(firstDate[0:8] + "01", "%Y-%m-%d")
    date2 = date1 + timedelta(days=1)
    date3 = date1 + timedelta(days=2)
    date4 = date1 + timedelta(days=3)
    date5 = date1 + timedelta(days=4)
    date6 = date1 + timedelta(days=5)
    date7 = date1 + timedelta(days=6)
    date8 = date1 + timedelta(days=7)
    date9 = date1 + timedelta(days=8)
    date10 = date1 + timedelta(days=9)
    date11 = date1 + timedelta(days=10)
    date12 = date1 + timedelta(days=11)
    date13 = date1 + timedelta(days=12)
    date14 = date1 + timedelta(days=13)
    date15 = date1 + timedelta(days=14)
    date16 = date1 + timedelta(days=15)
    date17 = date1 + timedelta(days=16)
    date18 = date1 + timedelta(days=17)
    date19 = date1 + timedelta(days=18)
    date20 = date1 + timedelta(days=19)
    date21 = date1 + timedelta(days=20)
    date22 = date1 + timedelta(days=21)
    date23 = date1 + timedelta(days=22)
    date24 = date1 + timedelta(days=23)
    date25 = date1 + timedelta(days=24)
    date26 = date1 + timedelta(days=25)
    date27 = date1 + timedelta(days=26)
    date28 = date1 + timedelta(days=27)
    date29 = date1 + timedelta(days=28)
    date30 = date1 + timedelta(days=29)
    date31 = date1 + timedelta(days=30)
    print(date31)

    context = {
        "podA": podA,
        "podB": podB,
        "restrPodA": restrPodA,
        "restrPodB": restrPodB,
        "today": today,
        'firstDate': firstDate,
        'parseDate': parseDate,
        "date1": date1,
        "date2": date2,
        "date3": date3,
        "date4": date4,
        "date5": date5,
        "date6": date6,
        "date7": date7,
        "date8": date8,
        "date9": date9,
        "date10": date10,
        "date11": date11,
        "date12": date12,
        "date13": date13,
        "date14": date14,
        "date15": date15,
        "date16": date16,
        "date17": date17,
        "date18": date18,
        "date19": date19,
        "date20": date20,
        "date21": date21,
        "date22": date22,
        "date23": date23,
        "date24": date24,
        "date25": date25,
        "date26": date26,
        "date27": date27,
        "date28": date28,
        "date29": date29,
        "date30": date30,
        "date31": date31,
    }

    return render(request, 'home/booking.html', context)


def booking_detailsPodA(request, selected_day):
    """ A view to return the about page """

    booking_id = uuid.uuid4().hex.upper()
    print(booking_id)

    one = selected_day
    date_one = datetime.strptime(one, "%Y-%m-%d")
    dep1 = date_one + timedelta(days=1)
    dep2 = date_one + timedelta(days=2)
    dep3 = date_one + timedelta(days=3)
    dep4 = date_one + timedelta(days=4)

    PodAnight_two = BookingPodA.objects.filter(arrival_date=dep1)
    PodAnight_three = BookingPodA.objects.filter(arrival_date=dep2)
    PodAnight_four = BookingPodA.objects.filter(arrival_date=dep3)

    context = {
        "booking_id": booking_id,
        "date_one": date_one,
        'dep1': dep1,
        'dep2': dep2,
        'dep3': dep3,
        'dep4': dep4,
        'PodAnight_two': PodAnight_two,
        'PodAnight_three': PodAnight_three,
        'PodAnight_four': PodAnight_four,
    }

    return render(request, 'home/booking_detailsPodA.html', context)


def booking_detailsPodB(request, selected_day):
    """ A view to return the about page """

    booking_id = uuid.uuid4().hex.upper()

    one = selected_day
    date_one = datetime.strptime(one, "%Y-%m-%d")
    dep1 = date_one + timedelta(days=1)
    dep2 = date_one + timedelta(days=2)
    dep3 = date_one + timedelta(days=3)
    dep4 = date_one + timedelta(days=4)

    PodBnight_two = BookingPodB.objects.filter(arrival_date=dep1)
    PodBnight_three = BookingPodB.objects.filter(arrival_date=dep2)
    PodBnight_four = BookingPodB.objects.filter(arrival_date=dep3)

    context = {
        "booking_id": booking_id,
        "date_one": date_one,
        'dep1': dep1,
        'dep2': dep2,
        'dep3': dep3,
        'dep4': dep4,
        'PodBnight_two': PodBnight_two,
        'PodBnight_three': PodBnight_three,
        'PodBnight_four': PodBnight_four,
    }

    return render(request, 'home/booking_detailsPodB.html', context)


def booking_savePodA(request):
    """ A view to return the about page """

    if request.method == 'POST':
        form = AddBookingPodAForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save()

            messages.success(request, 'Booking was succesfully created!')
            return redirect(reverse('booking_successPodA', args=[booking.id]))

        else:
            messages.error(request,
                           'Failed to create booking. \
                            Please ensure the form is valid.')
    else:
        form = AddBookingPodAForm()

    context = {
        'form': form
    }

    return render(request, 'home/booking_details.html', context)


def booking_savePodB(request):
    """ A view to return the about page """

    if request.method == 'POST':
        form = AddBookingPodBForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save()

            messages.success(request, 'Booking was succesfully created!')
            return redirect(reverse('booking_successPodB', args=[booking.id]))

        else:
            messages.error(request,
                           'Failed to create booking. \
                            Please ensure the form is valid.')
    else:
        form = AddBookingPodBForm()

    context = {
        'form': form
    }

    return render(request, 'home/booking_details.html', context)


def booking_successPodA(request, id):
    """ A view to return the index page """

    bookingPodA = get_object_or_404(BookingPodA, pk=id)

    context = {
        'bookingPodA': bookingPodA,
    }

    return render(request, 'home/booking_success.html', context)


def booking_successPodB(request, id):
    """ A view to return the index page """

    bookingPodB = get_object_or_404(BookingPodB, pk=id)

    context = {
        'bookingPodB': bookingPodB,
    }

    return render(request, 'home/booking_success.html', context)


def about(request):
    """ A view to return the about page """

    messages.success(request, 'Date restrictions was succesfully created!')

    return render(request, 'home/about.html')


def faq(request):
    """ A view to return the faq page """

    return render(request, 'home/faq.html')


def contact(request):
    """ A view to return the contact page """
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message_phone = request.POST['message_phone']
        message = request.POST['message']

        # to_email = 'nemeth.szilard82@gmail.com'
        to_email = DEFAULT_FROM_EMAIL

        subject = render_to_string(
            'home/contact_email/contact_email_subject.txt',
            {'message_name': message_name})

        body = render_to_string(
            'home/contact_email/contact_email_body.txt',
            {'message_name': message_name, 'message_email': message_email, 'message': message, 'message_phone': message_phone})

        # send an  contact email from contact us page
        send_mail(
            subject,
            body,
            'nemeth.szilard82@gmail.com',
            [to_email, 'nemeth.szilard82@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, f'Email sent!')

        return render(request, 'home/contact.html', {'message_name': message_name})

    else:
        return render(request, 'home/contact.html')


def planner(request):
    """ A view to return the faq page """


    nowDate = date.today()
    today = nowDate.strftime("%Y-%m-%d")
    print(today)

    bookPodA = BookingPodA.objects.filter(status="Booked")
    podA = list(bookPodA.values_list('arrival_range', flat=True))

    bookPodB = BookingPodB.objects.filter(status="Booked")
    podB = list(bookPodB.values_list('arrival_range', flat=True))

    date1 = datetime.strptime(today, "%Y-%m-%d")
    date2 = date1 + timedelta(days=1)
    date3 = date1 + timedelta(days=2)
    date4 = date1 + timedelta(days=3)
    date5 = date1 + timedelta(days=4)
    date6 = date1 + timedelta(days=5)
    date7 = date1 + timedelta(days=6)

    podA1 = BookingPodA.objects.filter(arrival_date=date1)
    podA2 = BookingPodA.objects.filter(arrival_date=date2)
    podA3 = BookingPodA.objects.filter(arrival_date=date3)
    podA4 = BookingPodA.objects.filter(arrival_date=date4)
    podA5 = BookingPodA.objects.filter(arrival_date=date5)
    podA6 = BookingPodA.objects.filter(arrival_date=date6)
    podA7 = BookingPodA.objects.filter(arrival_date=date7)

    podB1 = BookingPodB.objects.filter(arrival_date=date1)
    podB2 = BookingPodB.objects.filter(arrival_date=date2)
    podB3 = BookingPodB.objects.filter(arrival_date=date3)
    podB4 = BookingPodB.objects.filter(arrival_date=date4)
    podB5 = BookingPodB.objects.filter(arrival_date=date5)
    podB6 = BookingPodB.objects.filter(arrival_date=date6)
    podB7 = BookingPodB.objects.filter(arrival_date=date7)

    context = {
        "podA": podA,
        "podB": podB,
        "date1": date1,
        "date2": date2,
        "date3": date3,
        "date4": date4,
        "date5": date5,
        "date6": date6,
        "date7": date7,
        'podA1': podA1,
        'podA2': podA2,
        'podA3': podA3,
        'podA4': podA4,
        'podA5': podA5,
        'podA6': podA6,
        'podA7': podA7,
        'podB1': podB1,
        'podB2': podB2,
        'podB3': podB3,
        'podB4': podB4,
        'podB5': podB5,
        'podB6': podB6,
        'podB7': podB7,
    }

    return render(request, 'home/planner.html', context)


def reservation_details(request, booking_id):
    """ A view to return the edit booking page """

    reservation = get_object_or_404(BookingPodA, booking_id=booking_id)

    context = {
        'reservation':reservation,
        }

    return render(request, 'home/reservation_details.html', context)
