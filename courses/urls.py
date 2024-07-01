from django.urls import path

from .views import *

urlpatterns = [
    path('', allCourses, name="all_courses"),
]
