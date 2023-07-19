"""
Created on Tue Apr 18 15:30:47 2023

@author: LockheedMartin
"""
    
#%% Funktionen
#Definiton Name(Nachricht, Minimum, Maximum), msg specify
def input_int(msg, i_min, i_max):
    i=int(input(msg))
    
    while i<i_min or i>i_max:
        print("Error value!")
        i=int(input(msg))
    return i

my_int=input_int("Input number 10 ... 20 : ", 10, 20)
print(f"there's been an input: {my_int}")

#%% T4 A2
def input_int(msg, i_min, i_max):
    i=int(input(msg))
    while i<i_min or i>i_min:
        print("Please korrect value")
        i=int(input(msg))
    return i

#%% Use of own function

from input_tools import input_int

x4= input_int("VarianteD: ", 1, 10)

#%% prime Numbers: True/False
def check_prime(x):
    if x < 2:  # Numbers less than 2 are not prime
        return False
    for i in range(2, x):
        if x % i == 0:  # If x is divisible by any number from 2 to x-1, it is not prime
            return False
    return True

#p = check_prime(19)
#print(f"19 --> {p}")

#%% prime Numbers list:
def check_prime(x):
    if x < 2:  # Numbers less than 2 are not prime
        return False
    for i in range(2, x):
        if x % i == 0:  # If x is divisible by any number from 2 to x-1, it is not prime
            return False
    return True


for my_x in range(2, 20):
    p=check_prime(my_x)
    
    if p==True:
        print(f"{my_x}")


#%% T4 Ue1
#Funktion füllt eine Python-Liste mit n Zufallszahlen im Bereich von -10 bis 10 und gibt die gefüllte Liste als Rückgabewert zurück

import random

a=[]

x=1
while x<=10: 
    a.append(random.uniform(-10,10))
    x=x+1 

#print(f"{a}")

#Funktion sucht in der Liste das Element mit groessten Betrag

def max_abs(lst):
    for item in (lst):
        max_index=a.index(max(a))
        print(f"{max_index}")


#%% Error Code handeling general:
    
n=0
try:
    n=int(input("Input n: "))
    print(f"Input = {n}")

except ValueError:
    print("Check Value!")



