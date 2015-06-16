from app1.models import Library, Book
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    """
    A form used to fetch user personal details.
    :author Nourhan Fawzy:
    :param ModelForm:
    :return:
    """

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class LibraryForm(forms.ModelForm):
    """
    A form used to fetch user library details.
    :author Nourhan Fawzy:
    :param ModelForm:
    :return:
    """

    class Meta:
        model = Library
        fields = ('name', 'location')


class BookForm(forms.ModelForm):
    """
    A form used to fetch user book details.
    :author Nourhan Fawzy:
    :param ModelForm:
    :return:
    """

    class Meta:
        model = Book
        fields = ['name', 'year', 'about']
