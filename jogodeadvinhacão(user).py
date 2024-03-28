import random
erros = 0
ch = random.randrange(0,5)
ch1 = random.randrange(0,4)
ch2 = random.randrange(0,3)

pl1 = input("ja escolheu o numero ,se sim digite '1':")
if pl1 == '1':
 print("ta este é meu primeiro chute")
 print( str(ch))
 print("acertei?")
 ch2 = input("se sim digite 1, se nao digite 0:")
 if ch2 == '1':
  print("ok eu te venci HAHAHA ")
 elif ch2 == '0':
  erros+=1
  print("ta este é meu segundo chute:")
  print(ch1)
  ch5 = input("acertei?,se sim digite 1 ,se nao digite 0:")
  if ch5 == '1':
   print("ok")
  elif ch5 == '0':
   erros+=1 
  print("ta este é meu terceiro chute:")
  print(ch2)
  ch6 = input("acertei se sim digite 1 se nao digite 0:")
  if ch6 == '1':
   print("ok")
  elif  ch6 == '0':
   print("ok ,desito")
