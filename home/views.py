from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from blogs.models import Blog

def homePage(request):
    blogs = Blog.objects.all()[0:2]
    return render(request, 'home/home.html', {'blogs': blogs})

def contactMe(request):
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         message = form.cleaned_data['message']

    #         send_mail(
    #             f'Message from {name}',
    #             message,
    #             email,
    #             ['your_email@example.com'],
    #             fail_silently=False,
    #         )

    #         messages.success(request, 'Successfully sent!')
    #         return redirect('contact_me')
    # else:
    #     form = ContactForm()

    form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
    else:
        form = ContactForm

    return render(request, 'home/contact_me.html', {'form': form})
