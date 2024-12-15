from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import Game , Developer

def home(request):
    return render(request, 'home.html')

def list_games(request):
    games = Game.objects.all()
    return render(request, 'list_games.html', {'games': games})
#.select_related('author')
#def book_detail(request, book_id):
#  book = get_object_or_404(Book, pk=book_id)
  # return render(request, 'book_detail.html', {'book': book})
