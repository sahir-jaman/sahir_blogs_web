from django.urls import path

from .views import *

urlpatterns = [
    path('', allCourses, name="all_courses"),
    path('<int:course_id>/', courseDetail, name="course_detail"),
]
