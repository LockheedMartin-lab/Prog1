#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:30:47 2023

@author: LockheedMartin
"""

#%% List find & List find max: helpful example
shopping = ["bread", "jam", "marmite"]

trolley = []

for item in shopping:
    if item == "marmite":
        print ("Urgh! Yuck!")

else:
    print ("I'Yep let's get that")

#--------

# No Duplicates
a_list = [10, 11, 14, 23, 9, 3, 35, 22]
max_index = a_list. index (max(a_list))
print (f"{max_index}")
# Returns: 6
# Duplicates
a_list = [10, 11, 35, 14, 23, 9, 3, 35, 22]
indices = [index for index, item in enumerate(a_list) if item == max(a_list)]
print (indices)
# Returns: 12, 7]f



#%% Aufgabe 1 T3 | Funktion mit Plot & Beschriftung

#Bib import, plotten:
from matplotlib.pyplot import *

#Werte Spezifizieren, Anfang & Ende
x_start=float(input("x-Start: "))
x_end=float(input("x-End: "))


#While Function: zum durchlaufen der Funktion

while x_start <= x_end:
    y=2*pow(x_start, 2)-(x_start)-2
    print(f"{x_start:8.3f}{y:8.3f}")
    x_start=x_start+.25

#%% Aufgabe 2.5 T3 | Funktion mit Plot & Beschriftung

#Bib import, plotten:
import matplotlib.pyplot as plt
from math import sin, pi

#Werte Spezifizieren, Anfang & Ende
x_start=float(input("x-Start: "))
x_end=float(input("x-End: "))
#Schrittweite
x_step=float(input("x-increment: "))


#Erstellen von zwei Listen, x & y-Werte     
x_Values=[]
y_Values=[]


#While Function: zum durchlaufen der Funktion
    
while x_start <= x_end:
    y=sin(x_start)
    print(f"{x_start:8.3f} {y:8.3f}")
    x_start=x_start+x_step
    x_Values.append(x_start)
    y_Values.append(y)
        
        
#Koordinatensystem erstellen
plt.plot(x_Values, y_Values, "r--")
plt.grid(True)
plt.plot()
#Beschriftung des Koordinatensystems
plt.xlabel("x")
plt.ylabel("y")
plt.title("Traurige e-Funktion")   
    
