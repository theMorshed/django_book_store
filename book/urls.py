from django.urls import path
# from book.views import home, store_book, display_books, edit_book, delete_book, HomeTemplateView
# from book.models import BookStoreModel
# books = BookStoreModel.objects.all()
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('<int:num>/', views.HomeTemplateView.as_view(), {'author': 'morshed'}, name='homepage'),
    path('book_details/<int:id>', views.BookDetailsView.as_view(), name='book_details'),
    # path('store_book/', views.store_book, name='store_book'),
    path('store_book/', views.BookStoreFormView.as_view(), name='store_book'),
    path('display-book/', views.DisplayBookListView.as_view(), name='display_book'),
    # path('edit_book/<int:id>', views.edit_book, name='edit_book'),
    path('edit_book/<int:pk>', views.BookUpdateView.as_view(), name='edit_book'),
    # path('delete_book/<int:id>', views.delete_book, name='delete_book'),
    path('delete_book/<int:pk>', views.BookDeleteView.as_view(), name='delete_book'),
]
