from django.shortcuts import render

from .models import *


def allCourses(request):
    courses = Course.objects.all()
    return render(request, "courses/all_courses.html", {"courses": courses})
