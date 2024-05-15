from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'image','year','publishing_house','pages','dimensions','cover_type','price','genre']


