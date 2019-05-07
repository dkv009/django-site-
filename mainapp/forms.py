from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    fio = forms.CharField(help_text="Введите ФИО", label="ФИО")

    class Meta:
        model = User
        fields = ("username","password1","password2","email","fio",)


class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", 'password',)