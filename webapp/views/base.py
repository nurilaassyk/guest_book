from django.shortcuts import render
from webapp.models import Book


def home_view(request):
    book = Book.objects.order_by('-created_at').exclude(status='blocked')
    context = {
        'book': book
    }
    return render(request, 'index.html', context)
