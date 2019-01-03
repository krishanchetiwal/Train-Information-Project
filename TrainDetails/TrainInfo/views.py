from django.shortcuts import render
from .models import Traindetails

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            trains = Traindetails.objects.filter(name__icontains=q)
            return render(request, 'TrainInfo/search.html', {'trains': trains, 'query': q})
    return render(request, 'TrainInfo/home.html', {'error': error})
