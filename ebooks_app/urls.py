from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    # views.home means in views.py have home function on this function we defined home page response.
    path('contact',views.contact),
]
