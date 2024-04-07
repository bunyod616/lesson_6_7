from django.shortcuts import render
from django.views import View
from .models import Book
from django.http import HttpResponse

class BooksListView(View):
    def get(self, request):
        search = request.GET.get('search')
        if not search:
            books = Book.objects.all()
            context = {
                'books': books,
                'search': search
            }
            return render(request, 'library.html', context)
        else:
            books = Book.objects.filter(title__icontains=search)
            if books:
                context = {
                    'books': books,
                    'search': search
                }
                return render(request, 'library.html', context)
            else:
                return HttpResponse('<h1>No books found</h1>')
class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        return render(request, 'book_detail.html', {'book': book})