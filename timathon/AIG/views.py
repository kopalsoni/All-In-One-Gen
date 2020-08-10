from django.shortcuts import render
from .gen_files import quotes


def home(request):
    query = quotes.random_quote()
    print(query)
    return render(request, "home.html", {"data": query})


def about(request):
    return render(request, "about.html")
