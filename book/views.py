from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel

# Create your views here.
def home(request):
    return render(request, 'display_book.html')

def store_book(request):
    if request.method == 'POST':
        form = BookStoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_book')
    else:
        form = BookStoreForm()
    return render(request, 'store_book.html', {'form': form})

def display_books(request):
    books = BookStoreModel.objects.all()
    return render(request, 'display_book.html', {'books': books})

def edit_book(request, id):
    book = BookStoreModel.objects.get(pk = id)
    form = BookStoreForm(instance=book)
    if request.method == 'POST':
        form = BookStoreForm(request.POST, instance = book)
        if form.is_valid():
            form.save()
            return redirect('display_book')
    return render(request, 'store_book.html', {'form': form})

def delete_book(request, id):
    book = BookStoreModel.objects.get(pk = id).delete()
    return redirect('display_book')