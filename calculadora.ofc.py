num0 = int(input(":"))
num1 = input(":")
num2 = int(input(":"))
while True:
 s1 = num0 + num2
 s2 = num0 - num2
 s3 = num0 * num2
 s4 = num0 / num2
 if num1 == '+':
  print("resultado:   "+str(s1))
 elif num1 == '-':
  print("resultado:   "+str(s2))
 elif num1 == 'x':
  print("resultado:   "+str(s3))
 elif num1 == '/':
  print("resultado:   "+str(s4))
 else:
  print("caractere ínvalido!")