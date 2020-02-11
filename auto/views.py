from django.shortcuts import render, redirect
from .models import Car, Seller


def car_list(request):
    car = Car.objects.all()
    return render(request, 'car_list.html', {'car': car})