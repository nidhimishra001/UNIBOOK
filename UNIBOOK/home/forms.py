from home.models import Tag
from home.models import Book,Contact
from django.forms import ModelForm
from django import forms
from home import widgets

class BookForm(ModelForm):
    class Meta:
        model=Book
        fields='__all__'

class TagForm(ModelForm):
    class Meta:
        model=Tag
        fields='__all__'  


class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields='__all__'              