import random
import os

ak = 0
sort = random.randrange(0,100)
jg = int(input("digite seu numero:"))

while (sort!=jg) :
 os.system('cls')
 if sort>jg:
   print("ERRO , numero é maior")
 if sort<jg:
   print("ERRO , numero é menor")
   ak+=1
 jg = int(input("digite seu numero:"))


print("numero certo!")

