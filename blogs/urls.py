from django.urls import path
from .views import *


urlpatterns = [
    path('', blogList, name="blog_list")
]
