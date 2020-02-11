from django.shortcuts import render, redirect
from .models import Car, Seller


def car_list(request):
    cars = Cars.objects.all()
    return render(request, 'car_list.html', {'cars': car})