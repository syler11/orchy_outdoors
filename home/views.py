from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from orchy_outdoors.settings import DEFAULT_FROM_EMAIL
from home.models import BookingPodA, BookingPodB
from .forms import AddBookingPodAForm, AddBookingPodBForm

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

    dayPodA1 = BookingPodA.objects.filter(arrival_date=date1)
    dayPodA2 = BookingPodA.objects.filter(arrival_date=date2)
    dayPodA3 = BookingPodA.objects.filter(arrival_date=date3)
    dayPodA4 = BookingPodA.objects.filter(arrival_date=date4)
    dayPodA5 = BookingPodA.objects.filter(arrival_date=date5)
    dayPodA6 = BookingPodA.objects.filter(arrival_date=date6)
    dayPodA7 = BookingPodA.objects.filter(arrival_date=date7)
    dayPodA8 = BookingPodA.objects.filter(arrival_date=date8)
    dayPodA9 = BookingPodA.objects.filter(arrival_date=date9)
    dayPodA10 = BookingPodA.objects.filter(arrival_date=date10)
    dayPodA11 = BookingPodA.objects.filter(arrival_date=date11)
    dayPodA12 = BookingPodA.objects.filter(arrival_date=date12)
    dayPodA13 = BookingPodA.objects.filter(arrival_date=date13)
    dayPodA14 = BookingPodA.objects.filter(arrival_date=date14)
    dayPodA15 = BookingPodA.objects.filter(arrival_date=date15)
    dayPodA16 = BookingPodA.objects.filter(arrival_date=date16)
    dayPodA17 = BookingPodA.objects.filter(arrival_date=date17)
    dayPodA18 = BookingPodA.objects.filter(arrival_date=date18)
    dayPodA19 = BookingPodA.objects.filter(arrival_date=date19)
    dayPodA20 = BookingPodA.objects.filter(arrival_date=date20)
    dayPodA21 = BookingPodA.objects.filter(arrival_date=date21)
    dayPodA22 = BookingPodA.objects.filter(arrival_date=date22)
    dayPodA23 = BookingPodA.objects.filter(arrival_date=date23)
    dayPodA24 = BookingPodA.objects.filter(arrival_date=date24)
    dayPodA25 = BookingPodA.objects.filter(arrival_date=date25)
    dayPodA26 = BookingPodA.objects.filter(arrival_date=date26)
    dayPodA27 = BookingPodA.objects.filter(arrival_date=date27)
    dayPodA28 = BookingPodA.objects.filter(arrival_date=date28)
    dayPodA29 = BookingPodA.objects.filter(arrival_date=date29)
    dayPodA30 = BookingPodA.objects.filter(arrival_date=date30)
    dayPodA31 = BookingPodA.objects.filter(arrival_date=date31)


    dayPodB1 = BookingPodB.objects.filter(arrival_date=date1)
    dayPodB2 = BookingPodB.objects.filter(arrival_date=date2)
    dayPodB3 = BookingPodB.objects.filter(arrival_date=date3)
    dayPodB4 = BookingPodB.objects.filter(arrival_date=date4)
    dayPodB5 = BookingPodB.objects.filter(arrival_date=date5)
    dayPodB6 = BookingPodB.objects.filter(arrival_date=date6)
    dayPodB7 = BookingPodB.objects.filter(arrival_date=date7)
    dayPodB8 = BookingPodB.objects.filter(arrival_date=date8)
    dayPodB9 = BookingPodB.objects.filter(arrival_date=date9)
    dayPodB10 = BookingPodB.objects.filter(arrival_date=date10)
    dayPodB11 = BookingPodB.objects.filter(arrival_date=date11)
    dayPodB12 = BookingPodB.objects.filter(arrival_date=date12)
    dayPodB13 = BookingPodB.objects.filter(arrival_date=date13)
    dayPodB14 = BookingPodB.objects.filter(arrival_date=date14)
    dayPodB15 = BookingPodB.objects.filter(arrival_date=date15)
    dayPodB16 = BookingPodB.objects.filter(arrival_date=date16)
    dayPodB17 = BookingPodB.objects.filter(arrival_date=date17)
    dayPodB18 = BookingPodB.objects.filter(arrival_date=date18)
    dayPodB19 = BookingPodB.objects.filter(arrival_date=date19)
    dayPodB20 = BookingPodB.objects.filter(arrival_date=date20)
    dayPodB21 = BookingPodB.objects.filter(arrival_date=date21)
    dayPodB22 = BookingPodB.objects.filter(arrival_date=date22)
    dayPodB23 = BookingPodB.objects.filter(arrival_date=date23)
    dayPodB24 = BookingPodB.objects.filter(arrival_date=date24)
    dayPodB25 = BookingPodB.objects.filter(arrival_date=date25)
    dayPodB26 = BookingPodB.objects.filter(arrival_date=date26)
    dayPodB27 = BookingPodB.objects.filter(arrival_date=date27)
    dayPodB28 = BookingPodB.objects.filter(arrival_date=date28)
    dayPodB29 = BookingPodB.objects.filter(arrival_date=date29)
    dayPodB30 = BookingPodB.objects.filter(arrival_date=date30)
    dayPodB31 = BookingPodB.objects.filter(arrival_date=date31)


    context = {
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
        'dayPodA1': dayPodA1,
        'dayPodA2': dayPodA2,
        'dayPodA3': dayPodA3,
        'dayPodA4': dayPodA4,
        'dayPodA5': dayPodA5,
        'dayPodA6': dayPodA6,
        'dayPodA7': dayPodA7,
        'dayPodA8': dayPodA8,
        'dayPodA9': dayPodA9,
        'dayPodA10': dayPodA10,
        'dayPodA11': dayPodA11,
        'dayPodA12': dayPodA12,
        'dayPodA13': dayPodA13,
        'dayPodA14': dayPodA14,
        'dayPodA15': dayPodA15,
        'dayPodA16': dayPodA16,
        'dayPodA17': dayPodA17,
        'dayPodA18': dayPodA18,
        'dayPodA19': dayPodA19,
        'dayPodA20': dayPodA20,
        'dayPodA21': dayPodA21,
        'dayPodA22': dayPodA22,
        'dayPodA23': dayPodA23,
        'dayPodA24': dayPodA24,
        'dayPodA25': dayPodA25,
        'dayPodA26': dayPodA26,
        'dayPodA27': dayPodA27,
        'dayPodA28': dayPodA28,
        'dayPodA29': dayPodA29,
        'dayPodA30': dayPodA30,
        'dayPodA31': dayPodA31,
        'dayPodB1': dayPodB1,
        'dayPodB2': dayPodB2,
        'dayPodB3': dayPodB3,
        'dayPodB4': dayPodB4,
        'dayPodB5': dayPodB5,
        'dayPodB6': dayPodB6,
        'dayPodB7': dayPodB7,
        'dayPodB8': dayPodB8,
        'dayPodB9': dayPodB9,
        'dayPodB10': dayPodB10,
        'dayPodB11': dayPodB11,
        'dayPodB12': dayPodB12,
        'dayPodB13': dayPodB13,
        'dayPodB14': dayPodB14,
        'dayPodB15': dayPodB15,
        'dayPodB16': dayPodB16,
        'dayPodB17': dayPodB17,
        'dayPodB18': dayPodB18,
        'dayPodB19': dayPodB19,
        'dayPodB20': dayPodB20,
        'dayPodB21': dayPodB21,
        'dayPodB22': dayPodB22,
        'dayPodB23': dayPodB23,
        'dayPodB24': dayPodB24,
        'dayPodB25': dayPodB25,
        'dayPodB26': dayPodB26,
        'dayPodB27': dayPodB27,
        'dayPodB28': dayPodB28,
        'dayPodB29': dayPodB29,
        'dayPodB30': dayPodB30,
        'dayPodB31': dayPodB31,
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