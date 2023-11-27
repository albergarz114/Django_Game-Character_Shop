from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return HttpResponse('<h1>Welcome to the Game World!</h1>')

def character_list(request):
    return render(request,'game_app/character_list.html')

def detail(request):
    return render(request,'game_app/detail.html')
    
def games(request):
    return render(request, 'game_app/games.html')

