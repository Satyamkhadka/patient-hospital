from django.shortcuts import render
import requests

# Create your views here.
from django.http import HttpResponse
from diseases.models import Disease
from hospitals.models import Hospital


def check_if_nepal(data):
    if data["CountryCode"] == "NP":
        return True
    else:
        return False


def homepage(request):
    diseases_list = Disease.objects.order_by('-pub_date')[:3]
    hospitals_list = Hospital.objects.order_by('-pub_date')[:3]
    URL = "https://api.covid19api.com/summary"
    r = requests.get(url=URL)
    data = r.json()
    nepal = filter(check_if_nepal, data["Countries"])
    nepal = list(nepal)[0]
    nepal.pop('ID')
    nepal.pop('Country')
    nepal.pop('CountryCode')
    nepal.pop("Slug")
    nepal.pop("Premium")
    context = {'diseases_list': diseases_list,
               'hospitals_list': hospitals_list,
               'global_date': data["Global"].pop("Date")[:16],
               'global': data["Global"],
               'nepal_date': nepal.pop("Date")[:16],
               'nepal': nepal}
    return render(request, 'index.html', context)
