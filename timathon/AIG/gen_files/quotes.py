import requests
import json


def random_quote():
    url = "https://favqs.com/api/qotd"
    response = requests.request("GET", url)
    x = json.loads(response.text)
    return x["quote"]["body"]





