from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from blogs.models import Blog
from courses.models import Course

from django.db.models import Q

def homePage(request, slug=None):
    query = request.GET.get('query', '')

    if query:
        blogs = Blog.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        courses = Course.objects.filter(Q(title__icontains=query) | Q(introduction__icontains=query))
    else:
        blogs = Blog.objects.all()[:3]
        courses = Course.objects.all()[:3]

    context = {
        'blogs': blogs,
        'courses': courses,
    }
    return render(request, 'home/home.html', context)


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




def myServices(request):
    return render(request, 'home/services/my_services.html')



def search_results(request):
    query = request.GET.get('query', '')

    if query:
        # blogs = Blog.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        blogs = Blog.objects.filter(Q(title__icontains=query))
        # courses = Course.objects.filter(Q(title__icontains=query) | Q(introduction__icontains=query))
        courses = Course.objects.filter(Q(title__icontains=query))
    else:
        blogs = Blog.objects.none()
        courses = Course.objects.none()
    print("============blog===========", blogs)
    print("============courses===========", courses)

    context = {
        'blogs': blogs,
        'courses': courses,
    }
    return render(request, 'home/navbar/search_results.html', context)
