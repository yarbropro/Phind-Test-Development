from django.shortcuts import render
import json 
import requests 
import time
# Create your views here.

# def get_price(key):
#     while True:
#         data = requests.get(key)   
#         data = data.json()      
#         return data

def main(request):
    key = "https://api.binance.com/api/v3/ticker/price"
    butt = request.GET.get("button")
    
    # data = get_price(key)
    data = requests.get(key)
    data = data.json()
    if butt:
        print(butt)
        return render(request, "Main/index.html", {"data" : data, "pare" : butt})
    return render(request, "Main/index.html", {"data" : data, "pare" : "BTCUSDT"})