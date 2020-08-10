from django.shortcuts import render
import requests
import json
from . import quotes

def home(request):
    def random_quote():
        url = "https://favqs.com/api/qotd"
        response = requests.request("GET", url)
        x = json.loads(response.text)
        return x["quote"]["body"]

    query = quotes.random_quote()
    print(query)
    return render(request, "home.html", {"data": query})

def about(request): 
    return render(request,"about.html")