from django.shortcuts import render, redirect
from .models import Beer


def rating(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            beers = Beer.objects.order_by('-rating')
            return render(request, 'beer/rating.html', {'beers': beers})
        else:
            return redirect('/sign-in')
