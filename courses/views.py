from django.shortcuts import render, get_object_or_404

from .models import *


def allCourses(request):
    courses = Course.objects.all()
    return render(request, "courses/all_courses.html", {"courses": courses})


def courseDetail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    modules = Module.objects.filter(course=course)
    # sections = Section.objects.filter(module=modules)

    # print("====================courses==================", course)
    # for i in modules:
    #     print("====================Module=================", i)
    # for i in sections:
    #     print("====================section=================", i)


    context = {
        'course': course,
        'modules': modules,
    }

    return render(request, 'courses/course_detail.html', context )
