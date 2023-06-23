#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:30:47 2023

@author: alexanderaick
"""

#%%Mitternachtsformel
from math import *

a=float(input("Input value for a:"))
b=float(input("Input value for b:"))
c=float(input("Input value for c:"))
print("")

wurzel=b**2-4*a*c
if wurzel<0:
    print("Error Value sub 0")
    
elif wurzel==0:
    x= -b/(2*a)
    print(f"Dopelte NST bei x= {x}")
    
else:
    x1=(-b + sqrt(wurzel))/(2*a)
    x2=(-b - sqrt(wurzel))/(2*a)
    print(f"x1 = {x1}, x2= {x2}")
        
    

#%% Atmosphere
h=float(input("Input value for hight:"))

if h<0:
    print("Error, check value!")
    
elif h<=11019:
    t=-(143/22038)*h+15
    print(f"Die Temp betraegt: {t}")
    
elif h<=20063:
    t=-56.5
    print(f"Die Temp betraegt: {t}")
    
elif h<=32162:
    t=(23/24198)*h-75.07
    print(f"Die Temp betraegt: {t}")
    
elif h>32162:
    print("Value too high :/")


#%% Atmosphere
weiter = 1
while weiter == 1:
    
    h=float(input("Input value for hight:"))

    #test: print(f"{h}")


    error=False

    if h<0:
        print("Error, check value!")
        error=True
    
        
    elif h<=11019:
        starttemp=15
        startalt=0
        endtemp=-56.5
        endalt=11019
    
    elif h<=20063:
        starttemp=-56.5
        startalt=11019
        endtemp=-56.5
        endalt=20063
    
    elif h<=32162:
        starttemp=56.5
        startalt=20063
        endtemp=-44.5
        endalt=32162
    
    elif h<=47350:
        starttemp=-44.5
        startalt=32162
        endtemp=-2.5
        endalt=47350

    elif h<=51413:
        starttemp=-2.5
        startalt=47350
        endtemp=-2.5
        endalt=51413

    elif h<=71802:
        starttemp=-2.5
        startalt=51413
        endtemp=-58.5
        endalt=71802
        
    elif h<=86000:
        starttemp=-58.5
        startalt=71802
        endtemp=-86.2
        endalt=86000
        
    elif h>86000:
        print("Error, check value!")
        error=True
        
    
    # test: print(f"{starttemp}, {startalt}, {endtemp}, {endalt}")
    
    if not error:
        m=(endtemp - starttemp)/(endalt - startalt)
        t0=(endtemp)-(endalt*m)
        # test: print(f"{m}")
        t=m*h+t0
        print(f"Tepm betraegt {t:8.3f}")
    
    weiter = int(input("1 for another calculation, 0 to stop the run"))
    
#%% Energy Ex2 T2
h=float(input("Energy consumption in kWh: "))

i=1
while i==1:

    if h<0:
        print("Error")
    elif h<=2500:
        p=h*0.4
    elif h<= 5000:
        p=(h-2500)*0.35+2500*0.4
    elif h>5000:
        p=(h-5000)*0.3+2500*0.4+2500*0.35
    else:
        print("wtf???")

    print(f"Your energy cost: {p}")

    i=int(input("For another calc type 1, otherwise type 0"))
    
#%% Funktion allg: tabelle

#Funktionswerte ausgeben


xst=float(input("x-Start: "))
xed=float(input("x-End: "))


while xst <= xed:
    y=2*xst**2-xst-2
#    print(f"{xst} {y}")
    print(f"{xst:8.3f}{y:8.3f}")
    xst=xst+.25
    
    
#%% Arbeiten mit Listen allg


###Arbeiten mit Listen

#Erzeugen einer Liste mit vier Elementen
a = [1.1, 2.2, 3.3, 4.4]

#Erzeugen zwei leere Listen
b=[]
c=[]

#Fuege Elemente zur Liste hinzu
c.append(10)
c.append(20)
c.append(30)

#%% List find & List find max
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



#%%Plotten allg


from matplotlib.pyplot import *
#x-Werte
xx=[]
#y-Werte
yy=[]

#Speichere x- und y-Werte in Listen ab

x=-2
while x<= 2:
    y=x**2
    xx.append(x)
    yy.append(y)
    x=x+.5
    
#Zeichne Funktionsgraphen
plot(xx,yy, "r--")
grid(True)
show()

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


    
#%% Aufgabe 2 T3 | Funktion mit Plot & Beschriftung

#Bib import, plotten:
from matplotlib.pyplot import *

#Werte Spezifizieren, Anfang & Ende
x_start=float(input("x-Start: "))
x_end=float(input("x-End: "))



#Erstellen von zwei Listen, x & y-Werte     
x_Values=[]
y_Values=[]


#While Function: zum durchlaufen der Funktion

while x_start <= x_end:
    y=2*pow(x_start, 2)-(x_start)-2
    print(f"{x_start:8.3f}{y:8.3f}")
    x_start=x_start+.25
    x_Values.append(x_start)
    y_Values.append(y)


#Koordinatensystem erstellen
plot(x_Values, y_Values, "r--")
grid(True)
plot()
#Beschriftung des Koordinatensystems
xlabel("x")
ylabel("y")
title(f"Graph of the function y = 2x^2 - x - 2")   
    
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




#%% Resistors T5 A1 -> List give back smallest comp
#Best: Reference value
#anz: List size
#diff: List of sub values
#unt: difference risistorlist and wanted resistor
#posunt: positive version of unt (in case it's neg)
#l: run count, not needed cause of min()
#z: positon of min value in diff
#zw: value of min diffenrence 
#zwpr: percentage of min difference 
#db: Lowerst avalebale resistor Value 
#------------------------------------
#Liste mit Wiederstandswerten
werte=[10, 47, 100, 150, 220, 330, 470, 1000, 1500, 2200, 4700, 10000, 22000, 27000, 33000, 47000, 100000, 220000, 470000, 1000000]

#Besten Einzelwiderstand ermitteln (geringste Abweichng):
soll=int(input("Sollwert in Ohm: "))
Best=werte[0]
anz=len(werte)

diff=[]
l=0
for i in range(0, anz):
    unt=werte[i]-soll
    posunt=abs(unt)
    diff.append(posunt)
    #l=l+1 (not needed cause of min())

#findng the index of the lowest value
z=diff.index(min(diff))
zw=min(diff)
zwpr=zw*100/soll
db=werte[z]

print(f"Lowest resistor is {db}")
print(f"Difference: {zw} Ohm ({zwpr:.3}%)")



#%% Resistor T5 A2 mit def 
#Main prog
from input_tools import resistor_solo

soll=int(input("Sollwert in Ohm: "))
resistor_solo(soll)

#%% Resistor T5 A3 mit def
from input_tools import resistor_chain
from input_tools import resistor_solo
soll=int(input("Sollwert in Ohm: "))
print(" ")
resistor_chain(soll)
print(" ")
resistor_solo(soll)

#%% T5 A3 two intertwined loops

soll = int(input("Sollwert in Ohm: "))

werte = [10, 47, 100, 150, 220, 330, 470, 1000, 1500, 2200, 4700, 10000, 22000, 27000, 33000, 47000, 100000, 220000, 470000, 1000000]

diff = 1000000
diff = max(werte)
anz = len(werte)
r1no = 0
r2no = 0

for r1 in range(0, anz):
    for r2 in range(0, anz):
        unt = werte[r1] + werte[r2] - soll
        posunt = abs(unt)
        
        if posunt < diff:
            diff = posunt
            r1no = r1
            r2no = r2
            
r1value = werte[r1no]
r2value = werte[r2no]
r_total = r1value + r2value

print(f"Resistor 1: {r1value} Ohm")
print(f"Resistor 2: {r2value} Ohm")
print(f"Total Resistance: {r_total} Ohm")
print(f"Difference in Ohm: {diff}")
print(f"Difference in %: {diff / soll * 100}%")

#%% T5 A4 Parallel resistor 

soll = int(input("Sollwert in Ohm: "))

werte = [10, 47, 100, 150, 220, 330, 470, 1000, 1500, 2200, 4700, 10000, 22000, 27000, 33000, 47000, 100000, 220000, 470000, 1000000]

diff = 1000000
diff = max(werte)
anz = len(werte)
r1no = 0
r2no = 0

for r1 in range(0, anz):
    for r2 in range(0, anz):
        rges=(werte[r1]*werte[r2])/(werte[r1]+werte[r2])
        rdiff=rges-soll
        posrdiff = abs(rdiff)
        
        if posrdiff < diff:
            diff = posrdiff
            r1no = r1
            r2no = r2
            srges=rges



r1value = werte[r1no]
r2value = werte[r2no]

print(f"best paralell resistor combo: {r1value} and {r2value} Ohm.")
print(f"Total Resistance: {srges:.2f} Ohm")
print(f"Difference: {diff:.2f} Ohm ({diff / soll * 100:.2f}%)")


#%%





















