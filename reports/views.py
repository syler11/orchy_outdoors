from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta, datetime
from home.models import BookingPodA, BookingPodB
from django.db.models import Sum
from .reports import *

# Create your views here.
@login_required
def reports(request):
    """ A view to return the reports page """

    nowDate = datetime.now()
    this_year = int(nowDate.strftime("%Y"))

    today = nowDate.strftime("%Y-%m-%d")
    
  


    #March
    mar_start_date = f"{this_year}-04-01"
    mar_end_date = f"{this_year}-04-30"
    marchPodA = BookingPodA.objects.filter(status="Booked").filter(arrival_date__range=(mar_start_date, mar_end_date))
    marchPodB = BookingPodB.objects.filter(status="Booked").filter(arrival_date__range=(mar_start_date, mar_end_date))
    
    march_revPodA = sum(marchPodA.values_list('total_cost', flat=True))
    march_occPodA = sum(marchPodA.values_list('nights', flat=True))
    march_revPodB = sum(marchPodB.values_list('total_cost', flat=True))
    march_occPodB = sum(marchPodB.values_list('nights', flat=True))

    march_occTotal = march_occPodA + march_occPodB
    march_revTotal = march_revPodA + march_revPodB

    #April
    apr_start_date = f"{this_year}-04-01"
    apr_end_date = f"{this_year}-04-30"
    aprilPodA = BookingPodA.objects.filter(status="Booked").filter(arrival_date__range=(apr_start_date, apr_end_date))
    aprilPodB = BookingPodB.objects.filter(status="Booked").filter(arrival_date__range=(apr_start_date, apr_end_date))
    
    april_revPodA = sum(aprilPodA.values_list('total_cost', flat=True))
    april_occPodA = sum(aprilPodA.values_list('nights', flat=True))
    april_revPodB = sum(aprilPodB.values_list('total_cost', flat=True))
    april_occPodB = sum(aprilPodB.values_list('nights', flat=True))

    april_occTotal = april_occPodA + april_occPodB
    april_revTotal = april_revPodA + april_revPodB

    #May
    may_start_date = f"{this_year}-05-01"
    may_end_date = f"{this_year}-05-31"
    mayPodA = BookingPodA.objects.filter(status="Booked").filter(arrival_date__range=(may_start_date, may_end_date))
    mayPodB = BookingPodB.objects.filter(status="Booked").filter(arrival_date__range=(may_start_date, may_end_date))
    
    may_revPodA = sum(mayPodA.values_list('total_cost', flat=True))
    may_occPodA = sum(mayPodA.values_list('nights', flat=True))
    may_revPodB = sum(mayPodB.values_list('total_cost', flat=True))
    may_occPodB = sum(mayPodB.values_list('nights', flat=True))

    may_occTotal = may_occPodA + may_occPodB
    may_revTotal = may_revPodA + may_revPodB

    #June
    jun_start_date = f"{this_year}-06-01"
    jun_end_date = f"{this_year}-06-30"
    junePodA = BookingPodA.objects.filter(status="Booked").filter(arrival_date__range=(jun_start_date, jun_end_date))
    junePodB = BookingPodB.objects.filter(status="Booked").filter(arrival_date__range=(jun_start_date, jun_end_date))
    
    june_revPodA = sum(junePodA.values_list('total_cost', flat=True))
    june_occPodA = sum(junePodA.values_list('nights', flat=True))
    june_revPodB = sum(junePodB.values_list('total_cost', flat=True))
    june_occPodB = sum(junePodB.values_list('nights', flat=True))

    june_occTotal = june_occPodA + june_occPodB
    june_revTotal = june_revPodA + june_revPodB

    #July
    jul_start_date = f"{this_year}-07-01"
    jul_end_date = f"{this_year}-07-31"
    julyPodA = BookingPodA.objects.filter(status="Booked").filter(arrival_date__range=(jul_start_date, jul_end_date))
    julyPodB = BookingPodB.objects.filter(status="Booked").filter(arrival_date__range=(jul_start_date, jul_end_date))
    
    july_revPodA = sum(julyPodA.values_list('total_cost', flat=True))
    july_occPodA = sum(julyPodA.values_list('nights', flat=True))
    july_revPodB = sum(julyPodB.values_list('total_cost', flat=True))
    july_occPodB = sum(julyPodB.values_list('nights', flat=True))

    july_occTotal = july_occPodA + july_occPodB
    july_revTotal = july_revPodA + july_revPodB

    #August
    aug_start_date = f"{this_year}-08-01"
    aug_end_date = f"{this_year}-08-31"
    augustPodA = BookingPodA.objects.filter(status="Booked").filter(arrival_date__range=(aug_start_date, aug_end_date))
    augustPodB = BookingPodB.objects.filter(status="Booked").filter(arrival_date__range=(aug_start_date, aug_end_date))
    
    august_revPodA = sum(augustPodA.values_list('total_cost', flat=True))
    august_occPodA = sum(augustPodA.values_list('nights', flat=True))
    august_revPodB = sum(augustPodB.values_list('total_cost', flat=True))
    august_occPodB = sum(augustPodB.values_list('nights', flat=True))

    august_occTotal = august_occPodA + august_occPodB
    august_revTotal = august_revPodA + august_revPodB

    #September
    sep_start_date = f"{this_year}-09-01"
    sep_end_date = f"{this_year}-09-30"
    septemberPodA = BookingPodA.objects.filter(status="Booked").filter(arrival_date__range=(sep_start_date, sep_end_date))
    septemberPodB = BookingPodB.objects.filter(status="Booked").filter(arrival_date__range=(sep_start_date, sep_end_date))
    
    september_revPodA = sum(septemberPodA.values_list('total_cost', flat=True))
    september_occPodA = sum(septemberPodA.values_list('nights', flat=True))
    september_revPodB = sum(septemberPodB.values_list('total_cost', flat=True))
    september_occPodB = sum(septemberPodB.values_list('nights', flat=True))

    september_occTotal = september_occPodA + september_occPodB
    september_revTotal = september_revPodA + september_revPodB

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

    #Total
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

    context = {
        'this_year': this_year,
        'march_revPodA': march_revPodA,
        'march_occPodA': march_occPodA,
        'march_revPodB': march_revPodB,
        'march_occPodB': march_occPodB,
        'march_occTotal': march_occTotal,
        'march_revTotal': march_revTotal,
        'april_revPodA': april_revPodA,
        'april_occPodA': april_occPodA,
        'april_revPodB': april_revPodB,
        'april_occPodB': april_occPodB,
        'april_occTotal': april_occTotal,
        'april_revTotal': april_revTotal,
        'may_revPodA': may_revPodA,
        'may_occPodA': may_occPodA,
        'may_revPodB': may_revPodB,
        'may_occPodB': may_occPodB,
        'may_occTotal': may_occTotal,
        'may_revTotal': may_revTotal,
        'june_revPodA': june_revPodA,
        'june_occPodA': june_occPodA,
        'june_revPodB': june_revPodB,
        'june_occPodB': june_occPodB,
        'june_occTotal': june_occTotal,
        'june_revTotal': june_revTotal,
        'july_revPodA': july_revPodA,
        'july_occPodA': july_occPodA,
        'july_revPodB': july_revPodB,
        'july_occPodB': july_occPodB,
        'july_occTotal': july_occTotal,
        'july_revTotal': july_revTotal,
        'august_revPodA': august_revPodA,
        'august_occPodA': august_occPodA,
        'august_revPodB': august_revPodB,
        'august_occPodB': august_occPodB,
        'august_occTotal': august_occTotal,
        'august_revTotal': august_revTotal,
        'september_revPodA': september_revPodA,
        'september_occPodA': september_occPodA,
        'september_revPodB': september_revPodB,
        'september_occPodB': september_occPodB,
        'september_occTotal': september_occTotal,
        'september_revTotal': september_revTotal,
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
