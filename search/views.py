from django.shortcuts import render

from diseases.models import Disease
from hospitals.models import Hospital


def search(request):
    q = request.GET.get("q")
    if (q is None) or (q is ""):
        q = "23l23lk4l23kj4;3l2j4;l"
    diseases_list = Disease.objects.filter(name__icontains=q)
    hospitals_list = Hospital.objects.filter(name__icontains=q)
    print(hospitals_list)
    context = {
        'diseases_list': diseases_list,
        'hospitals_list': hospitals_list,
    }
    return render(request, 'search_results.html', context)
