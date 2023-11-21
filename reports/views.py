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

    context = {
        'this_year': this_year,
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
