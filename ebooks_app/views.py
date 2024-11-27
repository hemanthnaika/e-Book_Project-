from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
# from .models import Category
# Create your views here.
def home(request):
    # categories = Category.objects.all()
   
    carousel_items = [
        {
            "image_url": "https://via.placeholder.com/150",
            "title": "Card 1",
            "description": "Description for Card 1",
        },
        {
            "image_url": "https://via.placeholder.com/150",
            "title": "Card 2",
            "description": "Description for Card 2",
        },
        {
            "image_url": "https://via.placeholder.com/150",
            "title": "Card 3",
            "description": "Description for Card 3",
        },
        {
            "image_url": "https://via.placeholder.com/150",
            "title": "Card 4",
            "description": "Description for Card 4",
        },
    ]
    return render(request, "pages/home.html", {"carousel_items": carousel_items})

def books(request,id=None):
    carousel_items = [
        {
            "image_url": "https://via.placeholder.com/150",
            "title": "Card 1",
            "description": "Description for Card 1",
        },
        {
            "image_url": "https://via.placeholder.com/150",
            "title": "Card 2",
            "description": "Description for Card 2",
        },
        {
            "image_url": "https://via.placeholder.com/150",
            "title": "Card 3",
            "description": "Description for Card 3",
        },
        {
            "image_url": "https://via.placeholder.com/150",
            "title": "Card 4",
            "description": "Description for Card 4",
        },
    ]
    return render(request, "pages/books.html", {"carousel_items": carousel_items})

def book(request):
    carousel_items = [
        {
            "image_url": "https://via.placeholder.com/150",
            "title": "Card 1",
            "description": "Description for Card 1",
        },
        {
            "image_url": "https://via.placeholder.com/150",
            "title": "Card 2",
            "description": "Description for Card 2",
        },
        {
            "image_url": "https://via.placeholder.com/150",
            "title": "Card 3",
            "description": "Description for Card 3",
        },
        {
            "image_url": "https://via.placeholder.com/150",
            "title": "Card 4",
            "description": "Description for Card 4",
        },
    ]
    return render(request, "pages/book.html", {"carousel_items": carousel_items})
def checkout(request):
    return render(request, "pages/checkout.html")
def profile(request):
    return render(request, "pages/profile.html")
def order_success(request):
    return render(request, "pages/order_success.html")
def authors(request):
    return render(request, "pages/authors.html")
def author(request):
    return render(request, "pages/author.html")

def about(request):
    return render(request, "pages/about.html")
def contact(request):
    return render(request, "pages/contact.html")

