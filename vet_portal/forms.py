from django import forms
from django.contrib.auth.models import User
from .models import Profile, Patient, Appointment
from django.db.models import Q
from django.contrib.auth import authenticate


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic', 'mobile', 'address', 'city', 'state', 'zip')
        widgets = {
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip': forms.TextInput(attrs={'class': 'form-control'})
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        username_text = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user_name = User.objects.filter(Q(username=username_text)).first()
        if user_name:
            username = user_name.username
        else:
            raise forms.ValidationError("No user with this username or mobile.")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Username/password is incorrect")


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = {'name', 'age', 'profile', 'user'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'hidden': 'hidden'}),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = {'date', 'reason', 'patient', 'doctor'}
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'reason': forms.TextInput(attrs={'class': 'form-control'}),
            'patient': forms.TextInput(attrs={'hidden': 'hidden'}),
            'doctor': forms.TextInput(attrs={'hidden': 'hidden'}),
        }


