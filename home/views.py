from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from orchy_outdoors.settings import DEFAULT_FROM_EMAIL
from .models import Booking

from datetime import date, timedelta

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/home.html')

def booking(request):
    """ A view to return the booking page """

    today = date.today()
    dayDate = today.strftime("%Y-%m-%d")

    print(dayDate)

    date1 =  dayDate[0:8] + "01"
    date2 =  dayDate[0:8] + "02"
    date3 =  dayDate[0:8] + "03"
    date4 =  dayDate[0:8] + "04"
    date5 =  dayDate[0:8] + "05"
    date6 =  dayDate[0:8] + "06"
    date7 =  dayDate[0:8] + "07"
    date8 =  dayDate[0:8] + "08"
    date9 =  dayDate[0:8] + "09"
    date10 =  dayDate[0:8] + "10"
    date11 =  dayDate[0:8] + "11"
    date12 =  dayDate[0:8] + "12"
    date13 =  dayDate[0:8] + "13"
    date14 =  dayDate[0:8] + "14"
    date15 =  dayDate[0:8] + "15"
    date16 =  dayDate[0:8] + "16"
    date17 =  dayDate[0:8] + "17"
    date18 =  dayDate[0:8] + "18"
    date19 =  dayDate[0:8] + "19"
    date20 =  dayDate[0:8] + "20"
    date21 =  dayDate[0:8] + "21"
    date22 =  dayDate[0:8] + "22"
    date23 =  dayDate[0:8] + "23"
    date24 =  dayDate[0:8] + "24"
    date25 =  dayDate[0:8] + "25"
    date26 =  dayDate[0:8] + "26"
    date27 =  dayDate[0:8] + "27"
    date28 =  dayDate[0:8] + "28"
    date29 =  dayDate[0:8] + "29"
    date30 =  dayDate[0:8] + "30"
    

    day1 = Booking.objects.filter(arrival_date=date1)
    day2 = Booking.objects.filter(arrival_date=date2)
    day3 = Booking.objects.filter(arrival_date=date3)
    day4 = Booking.objects.filter(arrival_date=date4)
    day5 = Booking.objects.filter(arrival_date=date5)
    day6 = Booking.objects.filter(arrival_date=date6)
    day7 = Booking.objects.filter(arrival_date=date7)
    day8 = Booking.objects.filter(arrival_date=date8)
    day9 = Booking.objects.filter(arrival_date=date9)
    day10 = Booking.objects.filter(arrival_date=date10)
    day11 = Booking.objects.filter(arrival_date=date11)
    day12 = Booking.objects.filter(arrival_date=date12)
    day13 = Booking.objects.filter(arrival_date=date13)
    day14 = Booking.objects.filter(arrival_date=date14)
    day15 = Booking.objects.filter(arrival_date=date15)
    day16 = Booking.objects.filter(arrival_date=date16)
    day17 = Booking.objects.filter(arrival_date=date17)
    day18 = Booking.objects.filter(arrival_date=date18)
    day19 = Booking.objects.filter(arrival_date=date19)
    day20 = Booking.objects.filter(arrival_date=date20)
    day21 = Booking.objects.filter(arrival_date=date21)
    day22 = Booking.objects.filter(arrival_date=date22)
    day23 = Booking.objects.filter(arrival_date=date23)
    day24 = Booking.objects.filter(arrival_date=date24)
    day25 = Booking.objects.filter(arrival_date=date25)
    day26 = Booking.objects.filter(arrival_date=date26)
    day27 = Booking.objects.filter(arrival_date=date27)
    day28 = Booking.objects.filter(arrival_date=date28)
    day29 = Booking.objects.filter(arrival_date=date29)
    day30 = Booking.objects.filter(arrival_date=date30)

    print(day15)


    context = {
        "date1": date1,
        "date2": date2,
        "date3": date3,
        "date4": date4,
        "date5": date5,
        "date6": date6,
        "date7": date7,
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
        'day1': day1,
        'day2': day2,
        'day3': day3,
        'day4': day4,
        'day5': day5,
        'day6': day6,
        'day7': day7,
        'day8': day8,
        'day9': day9,
        'day10': day10,
        'day11': day11,
        'day12': day12,
        'day13': day13,
        'day14': day14,
        'day15': day15,
        'day16': day16,
        'day17': day17,
        'day18': day18,
        'day19': day19,
        'day20': day20,
        'day21': day21,
        'day22': day22,
        'day23': day23,
        'day24': day24,
        'day25': day25,
        'day26': day26,
        'day27': day27,
        'day28': day28,
        'day29': day29,
        'day30': day30,
        'dayDate': dayDate,
    }

    return render(request, 'home/booking.html', context)


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