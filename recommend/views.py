from django.shortcuts import render, redirect
from .functions import *
from beer.models import Beer
from user.models import User
from history.models import History


def home(request):
    if request.method == 'GET':
        user = request.user.is_authenticated

        if user:
            return redirect('/recommend')
        else:
            return redirect('/sign-in')


def recommend(request):
    if request.method == 'GET':
        return render(request, 'recommend/index.html')
    elif request.method == 'POST':
        style = request.POST.get('style', '')
        category = request.POST.get('category', '')
        aroma = request.POST.getlist('aroma')
        flavor = request.POST.getlist('flavor')
        season = request.POST.getlist('season')
        food = request.POST.getlist('food')
        body = request.POST.getlist('body')

        user_beer = [style, category, aroma, flavor, season, food, body]
        favorite_beer, score = find_favorite_beer(user_beer)

        favorite_beer = Beer.objects.get(name=favorite_beer)

        user = request.user

        history = History.objects.create(beer=favorite_beer, user=user)
        history.save()

        return render(request, 'recommend/result.html', {'beer': favorite_beer,
                                                         'score': score})
