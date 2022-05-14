from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from diseases.models import Disease
from hospitals.models import Hospital


def homepage(request):
    diseases_list = Disease.objects.order_by('-pub_date')[:3]
    hospitals_list = Hospital.objects.order_by('-pub_date')[:3]
    context = {'diseases_list': diseases_list,
               'hospitals_list': hospitals_list}
    return render(request, 'index.html', context)
