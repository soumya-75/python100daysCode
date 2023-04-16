#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PythonPassword Generator!")
nr_letters= int(input("How many total characters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password=[]
temp=nr_letters
k=temp-nr_numbers-nr_symbols
while nr_letters!=0:
  choice1=random.randint(0,2)
  if choice1==1 and nr_numbers!=0:
    c=random.randint(0,9)
    password.append(numbers[c])
    nr_numbers-=1
    nr_letters-=1
  if choice1==2 and nr_symbols!=0:
    c=random.randint(0,8)
    password.append(symbols[c])
    nr_symbols-=1
    nr_letters-=1
  if choice1==0 and k!=0:
    c=random.randint(0,51)
    password.append(letters[c])
    nr_letters-=1
    k-=1

str1=""
i=0
while i<temp:
  str1=str1+str(password[i])
  i+=1
print("Your Randomly generated password is "+str1)  