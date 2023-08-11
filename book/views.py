from typing import List
from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'home.html')

class HomeTemplateView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'name': 'django', 'age': 15}
        context.update(kwargs)
        return context
    
# def store_book(request):
#     if request.method == 'POST':
#         form = BookStoreForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('display_book')
#     else:
#         form = BookStoreForm()
#     return render(request, 'store_book.html', {'form': form})

# class BookStoreFormView(FormView):
#     template_name = 'store_book.html'
#     form_class = BookStoreForm
#     success_url = reverse_lazy('display_book')
    
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         form.save()
#         return redirect('display_book')

class BookStoreFormView(CreateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('display_book')

# def display_books(request):
#     books = BookStoreModel.objects.all()
#     return render(request, 'display_book.html', {'books': books})

class DisplayBookListView(ListView):
    model = BookStoreModel
    template_name = 'display_book.html'
    context_object_name = 'books'
    # ordering = ['-id']
    
    # def get_queryset(self):
    #     return BookStoreModel.objects.filter(author='Widoy rele')
    #     return BookStoreModel.objects.filter(id=678)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['books'] = BookStoreModel.objects.all().order_by('-book_name')
    #     context['books'] = BookStoreModel.objects.all().order_by('id')
    #     return context
    
    def get_template_names(self):
        if self.request.user.is_superuser:
            template_name = 'superuser.html'
        elif self.request.user.is_staff:
            template_name = 'staff.html'
        else:
            template_name = self.template_name
            
        return [template_name]
    
class BookDetailsView(DetailView):
    model = BookStoreModel
    template_name = 'book_details.html'
    context_object_name = 'book'
    pk_url_kwarg = 'id'

def edit_book(request, id):
    book = BookStoreModel.objects.get(pk = id)
    form = BookStoreForm(instance=book)
    if request.method == 'POST':
        form = BookStoreForm(request.POST, instance = book)
        if form.is_valid():
            form.save()
            return redirect('display_book')
    return render(request, 'store_book.html', {'form': form})

class BookUpdateView(UpdateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('display_book')

def delete_book(request, id):
    book = BookStoreModel.objects.get(pk = id).delete()
    return redirect('display_book')

class BookDeleteView(DeleteView):
    model = BookStoreModel
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('display_book')