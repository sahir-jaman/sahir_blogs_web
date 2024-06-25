from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'border-black focus:border-blue-500 focus:ring focus:ring-blue-200 focus:outline-none'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'border-black focus:border-blue-500 focus:ring focus:ring-blue-200 focus:outline-none'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'border-black focus:border-blue-500 focus:ring focus:ring-blue-200 focus:outline-none'
        })
    )
