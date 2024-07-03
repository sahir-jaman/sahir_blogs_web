from django.shortcuts import render, get_object_or_404

from .models import *


def allCourses(request):
    courses = Course.objects.all()
    return render(request, "courses/all_courses.html", {"courses": courses})


def courseDetail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course':course})
