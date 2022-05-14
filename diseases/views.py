from django.shortcuts import render

# Create your views here.

from .models import Disease


def disease(request, disease_id):
    disease = Disease.objects.get(pk=disease_id)
    context = {
        'disease': disease
    }
    return render(request, 'disease.html', context)


def diseases(request):
    query = request.GET.get("q")
    jump = 2
    if (query is None) or (query is ""):
        query = 0
    q = 0
    q = int(query)

    diseases_list = Disease.objects.order_by('-pub_date')[q:q+jump]
    next = q+jump
    prev = q-jump
    if prev < 0:
        prev = 0
    context = {
        'diseases_list': diseases_list,
        'q': q,
        'next': next,
        'prev': prev
    }
    return render(request, 'diseases.html', context)
