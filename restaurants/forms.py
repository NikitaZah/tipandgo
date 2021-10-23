from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Applicant, User
from django import forms


class ApplicationForm(ModelForm):
    class Meta:
        model = Applicant
        fields = ('first_name', 'last_name', 'phone', 'email', 'country', 'business_desc')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'name first', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'name last', 'placeholder': 'Last name'}),
            'phone': forms.TextInput(attrs={'class': 'full_width', 'placeholder': 'Phone number'}),
            'email': forms.TextInput(attrs={'class': 'full_width', 'placeholder': 'E-Mail'}),
            'country': forms.TextInput(attrs={'class': 'full_width', 'placeholder': 'Country'}),
            'business_desc': forms.TextInput(attrs={'class': 'full_width',
                                                    'placeholder': 'Tell us about your business'})
        }


class LoginForm(forms.Form):
    class Meta:
        phone = forms.CharField(max_length=16, label='Your phone number')
        password = forms.CharField(max_length=30, label='Your password')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        # password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        #     attrs={'class': 'field short first', 'placeholder': 'Password'}))
        # password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        #     attrs={'class': 'field short last', 'placeholder': 'Confirm password'}))
        fields = ('email', 'phone', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'field short first', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'field short last', 'placeholder': 'Last name'}),
            'phone': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Phone number'}),
            'email': forms.EmailInput(attrs={'class': 'field', 'placeholder': 'E-Mail'}),
            # 'password1': forms.PasswordInput(attrs={'class': 'field short first', 'placeholder': 'Password'}),
            # 'password2': forms.PasswordInput(attrs={'class': 'field short last', 'placeholder': 'Confirm password'}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'field short first', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'field short last', 'placeholder': 'Confirm password'})


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'phone')
