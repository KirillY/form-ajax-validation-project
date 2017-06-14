from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs) # override class
        self.fields.pop('password2') # remove default password2 field from the form
        # self.fields['password1'].label = "Пароль" # more visual to override with other class variables below
        self.fields['username'].widget.attrs['placeholder'] = 'Только английские буквы и цифры'
        self.fields['email'].widget.attrs['placeholder'] = 'example@email.com'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Только русские буквы'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Только русские буквы'
        self.fields['password1'].widget.attrs['placeholder'] = 'Не менее 5 символов'

    username = forms.CharField(required=True, label="Никнейм")
    email = forms.EmailField(required=True, label="Электронная почта")
    first_name = forms.CharField(required=False, label="Имя")
    last_name = forms.CharField(required=False, label="Фамилия")
    # password1 = forms.CharField(required=True, label="Пароль", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1') # define from fields

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
