import os
import sys
import time
os.system('clear')
#Welcoming User...
print("Welcome! To The World Of Random & Strong Password")
#Taking A Data
os.system('clear')
length =int(input("How Many Characters Will Be On Your Password ? : "))
#Importing Depen..
os.system('clear')
import random
import string
#Doing Some Process
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols
#Creating And Printing
print("Creating Password")
temp = random.sample(all,length)
print("Ready ?")
time.sleep(5)
password = "".join(temp)
print("Your Password Is Ready")
time.sleep(5)
os.system('clear')
print()
print()
print()
print()
print("The AutoGenreated Password For You", password)
print()
print()
print()
print()
time.sleep(10)
os.system('clear')
print("Thanks For Using")

time.sleep(0.10)
