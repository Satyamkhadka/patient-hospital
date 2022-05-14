from django.shortcuts import render

from diseases.models import Disease


def search(request):
    q = request.GET.get("q")
    if (q is None) or (q is ""):
        q = "23l23lk4l23kj4;3l2j4;l"
    diseases_list = Disease.objects.filter(name__icontains=q)
    context = {
        'diseases_list': diseases_list,
        # 'hospita_list':hospitals_list,
    }
    return render(request, 'search_results.html', context)
