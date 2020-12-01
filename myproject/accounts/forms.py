from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
# from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    dob = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1930, 2002)),
                          label=_('Date of birth:'))
    photo = forms.ImageField(required=False, label=_('Upload profile picture:'))

    class Meta:
        model = Profile
        fields = ['username', 'email', 'password1', 'password2', 'dob', 'photo']


class ProfileUpdateForm(ModelForm):
    dob = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1930, 2002)),
                          label=_('Date of birth:'))
    photo = forms.ImageField(required=False, label=_('Upload profile picture:'))

    class Meta:
        model = Profile
        fields = ['dob', 'photo']
