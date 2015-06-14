from app1.models import Library
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class LibraryForm(forms.ModelForm):

        class Meta:
            model = Library
            fields = ('name', 'location')
