import random
while True:
 words = 'abcdefghijklmnopqr6stuv76*4345766546&¨%$#@¨()3344¨¨%$#@!""12"!#wxyz1234567890?:><ABCD}{][{////*EFGHIJKLMNOPQRSTUVWXYZ'
 n1 = int(input("numero de caracteres:"))
 passwords = ''
 for c in range(n1):
  passwords += random.choice(words)
 print("aqui esta sua senha:   " + str(passwords))
