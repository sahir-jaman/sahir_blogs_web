from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

def homePage(request):
    context = {'hello': "yo"}
    return render(request, 'home/base.html', context)

def contactMe(request):

    form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
    else:
        form = ContactForm

    return render(request, 'home/contact_me.html', {'form': form})
