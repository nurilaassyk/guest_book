from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import BookForm
from webapp.models import Book


def add_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'add.html', context={'form': form})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            book = Book.objects.create(
                email=form.cleaned_data['email'],
                author=form.cleaned_data['author'],
                text=form.cleaned_data['text']
            )
            return redirect('home_view')
        else:
            return render(request, 'add.html', context={'form': form})


def update_view(request, id):
    book = get_object_or_404(Book, id=id)
    print(book)
    if request.method == 'GET':
        form = BookForm(initial={
            'email': book.email,
            'text': book.text,
            'author': book.author
        })
        context = {'form': form, 'book': book}
        print(context)
        return render(request, 'update.html', context={'form': form, 'book': book})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            book.title = form.cleaned_data['email']
            book.text = form.cleaned_data['text']
            book.author = form.cleaned_data['author']
            book.save()
            context = {'form': form, 'book': book}
            print(context)
            return redirect('home_view')
        else:
            return render(request, 'update.html', context={'form': form, 'book': book})


def delete_view(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'confirm_delete.html', context={'book': book})


def confirm_delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('home_view')
