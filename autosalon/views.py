from django.shortcuts import render
from .models import Brand, Car


def home(request):
    cars = Car.objects.all()
    brands = Brand.objects.all()
    context = {
        'brands': brands,
        'cars': cars
    }
    return render(request, 'index.html', context)

