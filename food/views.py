from django.shortcuts import render
from .models import Food


def food_list(request):
    food_list = Food.objects.all()
    context = {'food_list': food_list}
    return render(request, 'food_list.html', context)


def food_detail(request, slug):
    food = Food.objects.get(slug=slug)
    context = {'food': food}
    return render(request, 'food_detail.html', context)
