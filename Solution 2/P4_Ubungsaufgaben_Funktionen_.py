"""
Created on Sat Jul 15 22:05:15 2023

@author: User2
"""

#%% Übungsaufgabe 2

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
# len(n) -> gibt anzahl der elemente inder liste an  


if len(n) > 0:
    def min_max_abs(n):
        for item in (n):max_value = max(n)
        print("max_value: ", max_value)
        min_value = min(n)
        print("min_value: ", min_value)
        return min_value, max_value
    
    min_max_abs(n)
else:
    print("Liste ist leer") 
    


#%% Übungsaufgabe 3
n = 0

try:
    n = int(input("n eingeben: "))
    print("Eingabe = ", n)
    
except ValueError:
    print("Bitte gültige Zahl eingeben!")

#%% Übungsaufgabe 3

import random 

try:
    x1= int(input("x1 = "))
    x2= int(input("x2 = "))
    x3= int(input("x3 = "))
    
    n = [x1, x2, x3]


    if len(n) > 0:
        def min_max_abs(n):
            for item in (n):max_value = max(n)
            print("max_value: ", max_value)
            min_value = min(n)
            print("min_value: ", min_value)
            return min_value, max_value
    
        min_max_abs(n)
    else:
            print("Liste ist leer") 
            
except ValueError:
    print("Bitte gültige Zahl eingeben!")

# try: ... except ValueError:  -> falls ein falscher wert eingegeben wird (float statt int, buchstabe statt int, etc. ), programm abzubrechen
# und statt eine fehlermeldung auszugeben die Konsole zu bitten korrekte werte einzugeben












