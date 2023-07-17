"""
Created on Thu Jul 13 15:16:38 2023

@author: User2
"""
# Aufgabe 1

from math import *
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
print("")
wurzel = b**2 - 4 * a * c
if wurzel < 0:
    print("Keine reellen Nullstellen!")
else:
    if wurzel == 0:
        x = -b / (2*a)
        print(f"Doppelte Nullstelle bei x = {x}")
    else:
        x1 = (-b - sqrt(wurzel)) / (2*a)
        x2 = (-b + sqrt(wurzel)) / (2*a)
        print(f"Nullstellen bei x1 = {x1}, x2 = {x2}")
        
#%% verbesserte Varrainte von Aufgabe 1
from math import *
a = float(input("a: "))
b = float(input("b: ")) 
c = float(input("c: "))
print ("")
wurzel = b**2 - 4 * a * c
if wurzel < 0:
    print("Keine reellen Nulstellen vorhanden")
elif wurzel == 0:
    x = -b / (2*a)
    print(f"Doppelte Nullstelle bei x = {x}")
else: 
    x1 = (-b - sqrt(wurzel)) / (2*a)
    x2 = (-b + sqrt(wurzel)) / (2*a)
    print(f"Nullstellen bei x1 = {x1}, x2 = {x2}")

#%% Aufgabe 2
from math import *
g = float(input("Bitte geometr. Höhe in m eingeben: "))
if g < 0:
    print("Fehler: negative Höhe")
elif g > 23162:
    print("Fehlter: Wert für höhe zu groß")
elif g <= 11019:
    t = -(143/22038)*g+15
    print(f"Die Temperatur beträgt: {t}")
elif g <=20063:
    t= -(56.5)
    print(f"die Temperatur beträgt: {t}")
elif g <= 32162:
    t = (23/24198)*g-75.07
    print(f"Die Temperatur beträgt: {t}")

#%% Übungsaufgabe 1
from math import *
weiter = 1
while weiter == 1:
    g = float(input("Bitte geometr. Höhe in m eingeben: "))
    if g < 0:
        print("Fehler: negative Höhe")
    elif g > 47350:
        print("Fehlter: Wert für höhe zu groß")
    elif g <= 11019:
        starttemp=15
        startalt=0
        endtemp=56.5
        endalt=11019
        m=(endtemp - starttemp)/(endalt - startalt)
        t0=(endtemp)-(endalt*m)
        t=m*g+t0
        print(f"Temperatur beträgt: {t:8.3f}")
    elif g <= 20063:
        starttemp=56.5
        startalt=11.019
        endtemp=56.5
        endalt=20063
        m=(endtemp - starttemp)/(endalt - startalt)
        t0=(endtemp)-(endalt*m)
        t=m*g+t0
        print(f"Temperatur beträgt: {t:8.3f}")
    elif g <= 32162:
        starttemp=56.5
        startalt=20063
        endtemp=44.5
        endalt=32162
        m=(endtemp - starttemp)/(endalt - startalt)
        t0=(endtemp)-(endalt*m)
        t=m*g+t0
        print(f"Temperatur beträgt: {t:8.3f}")
    elif g <= 47350:
        starttemp=44.5
        startalt=32162
        endtemp=2.5
        endalt=47350
        m=(endtemp - starttemp)/(endalt - startalt)
        t0=(endtemp)-(endalt*m)
        t=m*g+t0
        print(f"Temperatur beträgt: {t:8.3f}")
    weiter = int(input("(1) nochmal oder (0) beenden: "))

#%% Übungsaufgabe 2
from math import *
weiter = 1
while weiter == 1:
    v = float(input("Bitte ihren Verbrauch in kWh eingeben: "))
    if v == 0:
        print("Ihr Preis beträgt Null")
    elif v <= 2500:
        p = v*0.40
        print(f"der Preis für ihren Verbrauch bertägt: {p:8.2f}")
    elif v <=5000:
        p = (v-2500)*0.35+2500*0.40
        print(f"der Preis für ihren Verbrauch bertägt: {p:8.2f}")
    elif v > 5000:
        p = 2500*0.40+2500*0.35+(v-5000)*0.30
        print(f"der Preis für ihren Verbrauch bertägt: {p:8.2f}")
    elif v == 0:
        Print("Ihr Preis beträgt Null")
    weiter = int(input("(1) nochmal oder (0) beenden: "))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    