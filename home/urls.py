from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name="home_page"),
    path('contact/', contactMe, name="contact_me"),
]
