from django import forms

from .models import Books

class BookForm(forms.ModelForm):

    class Meta:
        model = Books
        fields = ('author', 'title', 'year_of_create', 'publishing')