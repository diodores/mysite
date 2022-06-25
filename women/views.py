from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Страница приложения Women")


def categories(request, catid):
    return HttpResponse(f"<h1>Статья по категориям</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True) # permanent=True -  поменялся url на постоянно (301)
    return HttpResponse(f'Архив по годам {year}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')