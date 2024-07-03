from django.shortcuts import render, get_object_or_404
from .models import Blog

def blogList(request):
    blogs = Blog.objects.all()[0:6]
    return render(request, 'blogs/blogs.html', {'blogs': blogs})


def blogDetail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    print("===============================", blog)
    print("===============================", blog.title)
    return render(request, 'blogs/blog_detail.html', {'blog': blog})
