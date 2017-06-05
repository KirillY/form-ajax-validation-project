from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs) # override class
        self.fields.pop('password2') # remove default password2 field from the form
        self.fields['password1'].label = "Пароль"

    email = forms.EmailField(required=True, label="Электронная почта")
    first_name = forms.CharField(required=False, label="Имя")
    last_name = forms.CharField(required=False, label="Фамилия")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email') # define from fields
        # self.fields['email'].label = "Электронная почта"
        labels = { # override fields labels: "field_name":"new_label_name"
            "username": "Никнейм",
            "first_name": ("Имя"),
            "last_name": "Фамилия",
            "email":"Электронная почта",
            "password": "Пароль"
        }



    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
