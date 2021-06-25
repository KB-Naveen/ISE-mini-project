from django.shortcuts import render
import requests

key = "7841e24796f05e44b6956c2786d96e0828cf3e97"

# Create your views here.
def index(request):
    url = "https://api.nomics.com/v1/currencies/ticker?key="+key+"&convert=USD&per-page=15"
    res = requests.get(url).json()
    return render(request, 'index.html', {'res':res})

def coin(request,symbol):
    url1 = "https://api.nomics.com/v1/currencies/ticker?key=" + key + "&ids="+symbol+"&interval=1d&convert=USD"
    url2 = "https://api.nomics.com/v1/currencies?key=" + key + "&ids="+symbol
    csv_link = "https://query1.finance.yahoo.com/v7/finance/download/"+symbol+"-USD?period1=1420070400&period2=1624579200&interval=1d&events=history&includeAdjustedClose=true"
    res1 = requests.get(url1).json()
    res2 = requests.get(url2).json()
    return render(request, "coin.html", {'res1':res1, 'res2':res2, 'csv_link':csv_link})

def search(request):
    symbol = request.GET['symbol']
    symbol = symbol.upper()
    url1 = "https://api.nomics.com/v1/currencies/ticker?key=" + key + "&ids=" + symbol + "&interval=1d&convert=USD"
    url2 = "https://api.nomics.com/v1/currencies?key=" + key + "&ids=" + symbol
    csv_link = "https://query1.finance.yahoo.com/v7/finance/download/"+symbol+"-USD?period1=1420070400&period2=1624579200&interval=1d&events=history&includeAdjustedClose=true"
    res1 = requests.get(url1).json()
    res2 = requests.get(url2).json()
    return render(request, "coin.html", {'res1':res1, 'res2':res2, 'csv_link':csv_link})