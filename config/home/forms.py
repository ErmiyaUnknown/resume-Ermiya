from django import forms

from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'name' : 'name'}))
    last_name = forms.CharField(max_length=100, label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control', 'name' : 'family'}))
    email = forms.EmailField(max_length=100, label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'name' : 'email'}))
    phone_number = forms.CharField(max_length=20, label='Phone Number', widget=forms.TextInput(attrs={'class': 'form-control', 'name' : 'phone'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Message')

    class Meta:
        model = models.Message
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message']  # فیلدهایی که باید در فرم نمایش داده شوند