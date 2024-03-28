import random


player = input("p for paper, r for rock and s for scisors :")
computer = random.choice(['r','p','s'])
if (player == 'p' and computer == 'r') or (player == 'r' and computer == 's') or (player == 's' and computer == 'p'):
  print("win")
if (player == 'r' and computer == 'p') or (player == 's' and computer == 'r') or (player == 'p' and computer == 's'):
  print("lose")
if(player == computer):
 print("draw")