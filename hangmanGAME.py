import random
words = "albatroz","alce","alpaca","anaconda","anchova","andorinha","anta","antílope","aranha","babuíno","bacalhau","acuri","badejo","bagre","baiacu","baleia","barata","barbo","barracuda","beija-flor","besouro","bem-te-vi"
secretword = random.choice(words)
letter_usuario = []
ganhou =False

while True:

  
  print("")
  print("")

  tentativa = input("chute uma letra: ")
  ganhou=True
  letter_usuario.append(tentativa.lower())
  for letter in secretword:
    if letter in letter_usuario:
     print(letter)
    else:
     print("_")
     print("")

   

  for letter in secretword:
     if letter not in letter_usuario:
      ganhou = False
     
  if  ganhou :
     print(f"      A palavra era {secretword} , voce ganhou!!!")
     break
  