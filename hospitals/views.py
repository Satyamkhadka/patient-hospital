from django.shortcuts import render

# Create your views here.

from .models import Hospital


def hospital(request, hospital_id):
    hospital = Hospital.objects.get(pk=hospital_id)
    context = {
        'hospital': hospital
    }
    return render(request, 'hospital.html', context)


def hospitals(request):
    query = request.GET.get("q")
    jump = 2
    if (query is None) or (query is ""):
        query = 0
    q = 0
    q = int(query)

    hospitals_list = Hospital.objects.order_by('-pub_date')[q:q+jump]
    next = q+jump
    prev = q-jump
    if prev < 0:
        prev = 0
    context = {
        'hospitals_list': hospitals_list,
        'q': q,
        'next': next,
        'prev': prev
    }
    return render(request, 'hospitals.html', context)
