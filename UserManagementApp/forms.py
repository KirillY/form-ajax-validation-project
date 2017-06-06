from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs) # override class
        self.fields.pop('password2') # remove default password2 field from the form
        # self.fields['password1'].label = "Пароль" # more visual to override with other class variables below
        self.fields['username'].widget.attrs['placeholder'] = 'Begin with an English letter'
        self.fields['email'].widget.attrs['placeholder'] = 'Valid email address'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Russian letters only'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Russian letters only'
        self.fields['password1'].widget.attrs['placeholder'] = 'More than 5 symbols'

    username = forms.CharField(required=True, label="Никнейм")
    email = forms.EmailField(required=True, label="Электронная почта")
    first_name = forms.CharField(required=False, label="Имя")
    last_name = forms.CharField(required=False, label="Фамилия")
    password1 = forms.CharField(required=True, label="Пароль")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email') # define from fields

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
