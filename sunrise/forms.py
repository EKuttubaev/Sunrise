from django.contrib.auth.forms import UsernameField, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.views.generic import UpdateView

from sunrise.models import Products, Categories


class ProductForm(ModelForm):
    class Meta:
        model = Products
        exclude = ["created_date"]


class CategoryForm(ModelForm):
    class Meta:
        model = Categories
        exclude = []


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")
        fields_classes = {"username": UsernameField}


class SunriseUserEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        # exclude = []
        fields = ("username", "email",)
