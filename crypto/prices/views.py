from django.shortcuts import render
import requests

key = "7841e24796f05e44b6956c2786d96e0828cf3e97"

# Create your views here.
def index(request):
    url = "https://api.nomics.com/v1/currencies/ticker?key="+key+"&convert=USD&per-page=15"
    res = requests.get(url).json()
    return render(request, 'index.html', {'res':res})

def coin(request,symbol):
    url = "https://api.nomics.com/v1/currencies/ticker?key=" + key + "&ids="+symbol+"&interval=1d&convert=USD"
    res = requests.get(url).json
    return render(request, "coin.html", {'res':res})