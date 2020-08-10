from django.shortcuts import render
import requests
import json


def home(request):
    def random_quote():
        url = "https://favqs.com/api/qotd"
        response = requests.request("GET", url)
        x = json.loads(response.text)
        return x["quote"]["body"]

    query = random_quote()
    print(query)
    return render(request, "home.html", {"data": query})
