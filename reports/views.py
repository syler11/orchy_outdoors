from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta, datetime
from home.models import BookingPodA, BookingPodB
from django.db.models import Sum

# Create your views here.
@login_required
def reports(request):
    """ A view to return the reports page """

    nowDate = datetime.now()
    this_year = int(nowDate.strftime("%Y"))

    today = nowDate.strftime("%Y-%m-%d")
    
    podA = BookingPodA.objects.filter(status="Booked")
    total_costPodA = sum(podA.values_list('total_cost', flat=True))
    total_occPodA = sum(podA.values_list('nights', flat=True))
    podB = BookingPodB.objects.filter(status="Booked")
    total_costPodB = sum(podB.values_list('total_cost', flat=True))
    total_occPodB = sum(podB.values_list('nights', flat=True))

    total_cost = total_costPodA + total_costPodB
    total_occ = total_occPodA + total_occPodB

    podACancelled = BookingPodA.objects.filter(status="Cancel")
    total_costPodACancelled = sum(podACancelled.values_list('total_cost', flat=True))
    total_occPodACancelled = sum(podACancelled.values_list('nights', flat=True))
    podBCancelled = BookingPodB.objects.filter(status="Cancel")
    total_costPodBCancelled = sum(podBCancelled.values_list('total_cost', flat=True))
    total_occPodBCancelled = sum(podBCancelled.values_list('nights', flat=True))

    total_costCancelled = total_costPodACancelled + total_costPodBCancelled
    total_occCancelled = total_occPodACancelled + total_occPodBCancelled


    #October
    oct_start_date = f"{this_year}-10-01"
    oct_end_date = f"{this_year}-10-31"
    octoberPodA = BookingPodA.objects.filter(status="Booked").filter(arrival_date__range=(oct_start_date, oct_end_date))
    octoberPodB = BookingPodB.objects.filter(status="Booked").filter(arrival_date__range=(oct_start_date, oct_end_date))
    
    october_revPodA = sum(octoberPodA.values_list('total_cost', flat=True))
    october_occPodA = sum(octoberPodA.values_list('nights', flat=True))
    october_revPodB = sum(octoberPodB.values_list('total_cost', flat=True))
    october_occPodB = sum(octoberPodB.values_list('nights', flat=True))

    october_occTotal = october_occPodA + october_occPodB
    october_revTotal = october_revPodA + october_revPodB

    #November
    nov_start_date = f"{this_year}-11-01"
    nov_end_date = f"{this_year}-11-30"
    novemberPodA = BookingPodA.objects.filter(status="Booked").filter(arrival_date__range=(nov_start_date, nov_end_date))
    novemberPodB = BookingPodB.objects.filter(status="Booked").filter(arrival_date__range=(nov_start_date, nov_end_date))
    
    november_revPodA = sum(novemberPodA.values_list('total_cost', flat=True))
    november_occPodA = sum(novemberPodA.values_list('nights', flat=True))
    november_revPodB = sum(novemberPodB.values_list('total_cost', flat=True))
    november_occPodB = sum(novemberPodB.values_list('nights', flat=True))

    november_occTotal = november_occPodA + november_occPodB
    november_revTotal = november_revPodA + november_revPodB

    context = {
        'this_year': this_year,
        'october_revPodA': october_revPodA,
        'october_occPodA': october_occPodA,
        'october_revPodB': october_revPodB,
        'october_occPodB': october_occPodB,
        'october_occTotal': october_occTotal,
        'october_revTotal': october_revTotal,
        'november_revPodA': november_revPodA,
        'november_occPodA': november_occPodA,
        'november_revPodB': november_revPodB,
        'november_occPodB': november_occPodB,
        'november_occTotal': november_occTotal,
        'november_revTotal': november_revTotal,
        'total_costPodA': total_costPodA,
        'total_occPodA': total_occPodA,
        'total_costPodB': total_costPodB,
        'total_occPodB': total_occPodB,
        'total_cost': total_cost,
        'total_occ': total_occ,
        'total_costPodACancelled': total_costPodACancelled,
        'total_occPodACancelled': total_occPodACancelled,
        'total_costPodBCancelled': total_costPodBCancelled,
        'total_occPodBCancelled': total_occPodBCancelled,
        'total_costCancelled': total_costCancelled,
        'total_occCancelled': total_occCancelled,
    }

    return render(request, 'reports/reports.html', context)
