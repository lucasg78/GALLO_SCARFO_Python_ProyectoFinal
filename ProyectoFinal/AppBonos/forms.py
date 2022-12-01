from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppBonos.models import Avatar


class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
        help_texts = {k: "" for k in fields}


class UserEditionForm(UserCreationForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}


class AvatarForm(forms.Form):

    imagen = forms.ImageField(required=True)

    class Meta:
        model = Avatar
        fields = ["imagen", "user"]
