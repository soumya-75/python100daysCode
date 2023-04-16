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
import random
choice=int(input("What do you choose, Type 0 for Rock, 1 for Paper, 2 for Scissors \n"))
comp= random.randint(0,2)
if choice==0:
  print(rock)
if choice==1:
  print(paper)
if choice==2:
  print(scissors)
print("\n Computer Chose")
if comp==0:
  print(rock)
if comp==1:
  print(paper)
if comp==2:
  print(scissors)
print("\n")

if choice==0:
  if comp==0:
    print("Draw")
  if comp==1:
    print("Computer Wins")
  if comp==2:
    print("You Win")

if choice==1:
  if comp==2:
    print("Computer Wins")
  if comp==1:
    print("Draw")
  if comp==0:
    print("You Win")

if choice==2:
  if comp==2:
    print("Draw")
  if comp==0:
    print("Computer Wins")
  if comp==1:
    print("You Win")
    



