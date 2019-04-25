from django.shortcuts import render
from .models import Shirt
from django.urls import Resolver404
from django.http import Http404


def main(request):
    three_shirts = []
    row = 0
    col = 0
    shirts = Shirt.objects.all()
    for shirt in shirts:
        if col == 0:
            three_shirts.append([shirt])
            col += 1
        elif col == 2:
            three_shirts[row].append(shirt)
            col = 0
            row += 1
        else:
            three_shirts[row].append(shirt)
            col += 1

    return render(request, 'main.html', {'shirts': three_shirts})


def shirt(reqiest, shirt_id):
    try:
        shirt = Shirt.objects.get(id=shirt_id)
    except Resolver404:
        Http404
    return render(reqiest, 'shirt.html', {'shirt': shirt})


def edit_shirt(reqiest, shirt_id):
    try:
        shirt = Shirt.objects.get(id=shirt_id)
    except Resolver404:
        Http404
    return render(reqiest, 'edit_shirt.html', {'shirt': shirt})
