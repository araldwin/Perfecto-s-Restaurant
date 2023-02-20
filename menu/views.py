from django.shortcuts import render
from .models import Menu


def menu_list(request):
    menu_list = Menu.objects.all()

    return render(request, 'menu/menu.html', {'menu_list': menu_list})


def menu_detail(request, slug):
    menu_detail = Menu.objects.get(slug=slug)

    return render(request, 'menu/detail.html', {'menu_detail': menu_detail})