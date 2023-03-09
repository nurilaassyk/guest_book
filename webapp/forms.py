from django.forms import ModelForm, Textarea
from webapp.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('author', 'text', 'email')
        widgets = {
            'text': Textarea(attrs={'cols': 50, 'rows': 10}),

        }
