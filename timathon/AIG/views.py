from django.shortcuts import render
from .gen_files import quotes, rand_images


def home(request):
    quote_query = quotes.random_quote()
    rand_images.random_images()
    return render(request, "home.html", {"data": quote_query, })


def about(request):
    return render(request, "about.html")
