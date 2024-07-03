from django.urls import path
from .views import *


urlpatterns = [
    path('', blogList, name="blog_list"),
    path('<int:blog_id>/', blogDetail, name="blog_detail"),
]
