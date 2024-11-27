from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('books/', views.books, name='all_books'),
    path('books/<uuid:id>/', views.books, name='books'),
    path('book/', views.book, name='book'),
    path('authors/', views.authors, name='authors'),
    path('author/', views.author, name='author'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
    path('profile/', views.profile, name='profile'),
    path('order_success/', views.order_success, name='order_success'),
]
