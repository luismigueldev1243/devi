

ste = True
while True:
 print("1: letters counter")
 print("2: simbles\letters replacer:  ")
 print("3: lowercase to uppercase:  ")
 print("4: uppercase to lowercase:  ")
 print("")
 print("")
 perg = input("write 1 to select 1, 2 to select 2,3 to select 3,4 to select 4: ")
 if perg =='1':
  words = input("text here: ")
  print(len(words)-words.count(" "))
 if perg =='2':
  words2 = input("text here: ")
  a = input("simble1: ")
  b = input("simble2:")
  print(words2.replace(a,b))
 if perg == '3': 
  words3 = input("text here: ")
  print(words3.upper())
 if perg == '4':
  words4 = input("text here: ")
  print(words4.lower())
 
