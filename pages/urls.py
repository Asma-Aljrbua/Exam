from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("list/", views.list_games, name="list_games"),
   # path('books/<int:book_id>/', views.book_detail, name='book_detail'),
]
