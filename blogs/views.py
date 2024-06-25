from django.shortcuts import render
from .models import Blog

def hello(request):
    # Retrieve all blogs from the database
    blogs = Blog.objects.all()

    # Render the 'blogs.html' template with the list of blogs
    return render(request, 'blogs.html', {'blogs': blogs})
