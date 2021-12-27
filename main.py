import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_img =[rock, paper, scissors]
choose = int(input("what do you choose? Type '0' for rock, '1' for paper, '2' for scissors\n"))

if choose >= 3 or choose < 0:
  print("Y0u lose inviled number")
else:
  print("you chose")
  print(game_img[choose])

  computer = random.randint(0,2)
  print(game_img[computer])
  print(f"Computer chose {computer}")

  if choose == 0 and computer == 2:
    print("you win")
  elif computer == 2 and choose == 0:
    print("you lose")
  elif choose < computer:
    print("you lose")
  elif choose > computer:
    print("you win")
  elif computer > choose:
    print("you win")
  elif choose == computer:
    print("its a draw")

