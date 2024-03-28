import requests
import json
print("cotacao das moedas:")
rq = requests.get( "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
rq = rq.json()
cot_dol = rq['USDBRL']["bid"]
print("dolar :" + str(cot_dol))