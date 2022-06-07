from django.shortcuts import render, redirect
from .models import Beer
import csv

# Create your views here.
path = "templates/맥주_cbf_data.csv"
file = open(path, encoding='UTF-8')
reader = csv.reader(file)
for i, row in enumerate(reader):
    if i > 0:
        Beer.objects.create(
            name = row[3],
            style = row[4],
            category = row[5],
            aroma = row[6],
            flavor = row[7],
            balance = row[8],
            season = row[9],
            paring_food = row[10],
            body = row[11],
            rating = row[12],
        )

def rating(request):
    if request.method == 'GET':
        beers = Beer.objects.order_by('-rating')
        print(beers)
    return render(request, 'beer/rating.html', {'beers': beers})
