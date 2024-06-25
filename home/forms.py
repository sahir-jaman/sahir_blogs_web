# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'w-full p-3', 'placeholder': 'Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'w-full p-3', 'placeholder': 'Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'w-full p-3', 'placeholder': 'Message'}), required=True)
