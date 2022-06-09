from django.shortcuts import render
from .functions import *


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
        favorite_beer = find_favorite_beer(user_beer)

        favorite_beer = Beer.objects.get(name=favorite_beer)

        return render(request, 'recommend/result.html', {'beer': favorite_beer})
