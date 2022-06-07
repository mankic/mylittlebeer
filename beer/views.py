from django.shortcuts import render, redirect
from .models import Beer


def rating(request):
    if request.method == 'GET':
        beers = Beer.objects.order_by('-rating')
        print(beers)
    return render(request, 'beer/rating.html', {'beers': beers})
