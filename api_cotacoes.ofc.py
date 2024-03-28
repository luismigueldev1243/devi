import requests
import json
from tkinter import *

def printr():
 text6 = Label(janela,text="cotacoes das moedas:")
 rq = requests.get( "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
 rq = rq.json()
 cot_dol1 = rq['USDBRL']["bid"]
 cot_dol2 = rq['EURBRL']["bid"]
 cot_dol3 = rq['BTCBRL']["bid"]
 
 text1 =Label(janela,text="dolar: " + cot_dol1)
 text1.grid(column=1,row=2)
 text2 =Label(janela,text="euro: " + cot_dol2)
 text2.grid(column=1,row=3)
 text3 =Label(janela,text="bitcoin: " + cot_dol3)
 text3.grid(column=1,row=4)

janela = Tk()
janela.geometry("250x250")
text = Label(janela,text="ola")
text.grid(column=0,row=0,padx=10,pady=10)
bot = Button(janela,text="clique aqui",command=printr)
bot.grid(column=1,row=1)
janela.mainloop()


