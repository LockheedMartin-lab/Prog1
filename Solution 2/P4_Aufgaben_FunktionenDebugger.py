"""
Created on Fri Jul 14 13:55:26 2023

@author: User2
"""

#%% Aufgabe 1 - Eingabe von ganzen Zahlen 
def input_int(msg, i_min, i_max):       
    i = int(input(msg))
    while i < i_min or i > i_max:
            print("Bitte korrekten Wert eingeben!")
            i = int(input(msg))
    return i
    
my_int = input_int("Zahl 10 ... 20 eingeben: "
, 10, 20)
print(f"Es wurde {my_int} eingegeben") 

#msg = "zahl 10 ... 20 eingeben"
#i_min = 10 
# i_max = 20 -> steht bei input_int Zeile 15 hinter den "" 


#%% Aufgabe 4a: Primzahlen - Wahr/Falsch
x = int(input("Zahl eingeben: "))
def check_prime(x):
    if x < 2: 
        return False
    for i in range(2, x):
        if x % i ==0:
            return False
    return True 
p= check_prime(x)
print(f"{x} --> {p}")



#%% Übungsaufgabe 1
# n-Zufallszahlen in einer Liste

import random 
a=[]

x = 1
while x <= 10:
    a.append(random.uniform(-10,10))
    x=x+1

#print(f"{a}")

# limit - Zufallszahlen in einer Liste, Verbessert
import random 
start = -10
stop = 10
limit = 10
#limit = wie viele zahlen ausgegeben 

c = [random.randint(start,stop)for iter in range(limit)]
# random.randint gibt der liste die zufallswerte als integer
# alles was in [] gespeichet wird -> Liste

#print ("c: ", c)

#sucht maximalen WERT in Liste
def max_abs(c):
    for item in (c):
        max_value = max(c)
        print("max_value: ", max_value)
        return c
max_abs(c)

#sucht maximalen INDEX in Liste
max_value = max(c)
def max_abs(c):
    for item in (c):
        max_index = c.index(max_value)
        print("max_index: ", max_index)
        return c
max_abs(c)


#%% ADD
# skript das fill_rand() und max_abs() verwendet
import random 

n = []

def fill_rand(n):
    for i in range(0,10):
        x = random.randint(1,30)
        n.append(x)
    print ("Anzahl n: ", len(n))
    return n
fill_rand(n)
# range(0,10) -> die liste ist 10 Werte lang
# x = random.randint (start,stop) -> x wird random integer zwischen 1 bis 30 zugeschreiben 
# x -> so oft neu zugeteilt bis die liste mit allen werten (z.b. 10) voll ist weil range(0,10)
# n.append(x) -> der liste n werden die werte von x zugeteilt bis sie voll ist

def max_abs(n):
    for item in (n):
        max_value = max(n)
        print("max_value: ", max_value)
        return n

max_abs(n)

# len(n) -> gibt anzahl der elemente inder liste an  