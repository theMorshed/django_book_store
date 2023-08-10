from django.urls import path
from book.views import home, store_book, display_books, edit_book, delete_book

urlpatterns = [
    path('', display_books, name='homepage'),
    path('store_book/', store_book, name='store_book'),
    path('display-book/', display_books, name='display_book'),
    path('edit_book/<int:id>', edit_book, name='edit_book'),
    path('delete_book/<int:id>', delete_book, name='delete_book'),
]
