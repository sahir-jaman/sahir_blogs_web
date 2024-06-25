from django.shortcuts import render
from .models import Blog

def blogList(request):
    # Retrieve all blogs from the database
    blogs = Blog.objects.all()[0:6]

    # Render the 'blogs.html' template with the list of blogs
    return render(request, 'blogs/blogs.html', {'blogs': blogs})
