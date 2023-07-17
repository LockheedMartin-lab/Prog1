"""
Created on Fri Jul 14 11:26:56 2023

@author: User2
"""
#%% Aufgabe 1 
from math import *
x = -2
while x <= 2:
    y = 2 * x - 2
    print(f"{x} {y}")
    x = x + 0.25

#%% Aufgabe 1 verbessert
from math import *
x_start = float(input("x-Start: "))
x_ende = float(input("x-Ende: "))
while x_start <= x_ende:
    y = 2 * x_start**2 - x_start - 2
    print(f" {x_start:8.3f}   {y:8.3f}")
    x_start = x_start + 0.25


#%% Aufgabe 2
from math import *
from matplotlib.pyplot import *
x_start = float(input("x-Start: "))
x_ende = float(input("x-Ende: "))
#Estellen von zwei listen 
x_Values=[]
y_Values=[]

while x_start <= x_ende:
    y = 2 * x_start**2 - x_start - 2
    print(f" {x_start:8.3f}   {y:8.3f}")
    x_start = x_start + 0.25
#.append -> macht den graph erst sichtbar/ gibt zahlen den listen und dem "plot"
    x_Values.append(x_start)
    y_Values.append(y)

# Koordinatensystem erstellen 
plot(x_Values, y_Values, "r--")
grid(True)
plot()

# Beschriftung des Koordinatensystems
xlabel("x")
ylabel("y")
title(f"Graph der Funktion y = 2x^2 - x - 2")



from matplotlib.pyplot import *
from math import sin, pi

x_start = float(input("x-Start: "))
x_ende = float(input("x-Ende: "))

#Schrittweite des graphen 
x_step=float(input("x-Schrittgröße: "))

#Liste erstellen 
x_Values = []
y_Values = []

while x_start <= x_ende:
    y = sin(x_start)
    print(f" {x_start:8.3f}   {y:8.3f}")
    x_start = x_start + x_step
#.append -> macht den graph erst sichtbar/ gibt zahlen den listen und dem "plot"
    x_Values.append(x_start)
    y_Values.append(y)
    
#Koordinatensystem erstellen
plot(x_Values, y_Values, "r--")
grid(True)
plot()

#Beschriftung des Korrdinatensystems
xlabel("x")
ylabel("y")
title("Sinusfunktion")

#%% Übungsaufgabe 1
import matplotlib.pyplot as plt
from math import sin, pi, cos
t_start = float(input("start Zeit: "))
t_ende = float(input("ende Zeit: "))
t_step = float(input("Schrittgröße: "))


#Liste erstellen 
uxValues = []
uyValues  = []
ixValues  = []
iyValues  = []
pxValues  = []
pyValues  = []


while t_start <= t_ende:
    f = 50
    u = 10*sin(2*pi*f*t_start)
    i = pi*cos(2*pi*f*t_start)
    p = u * i 
    print("t_start:", t_start)
    t_start = t_start + t_step
    print("u:",u)
    t_start = t_start + t_step
    print("i:", i)
    t_start = t_start + t_step
    print("p:", p)
    t_start = t_start + t_step
    
    uxValues .append(t_start)
    uyValues .append(u)
    
    ixValues .append(t_start)
    iyValues .append(i)
    
    pxValues .append(t_start)
    pyValues .append(p)
    

#Koordinatensystem erstellen 
plt.plot(uxValues , uyValues , "b-")
plt.plot(ixValues , iyValues , "r--")
plt.plot(pxValues , pyValues , "g--")
plt.grid(True)
plt.plot()

#Beschriftung des koordinatensystems
plt.xlabel("x")
plt.ylabel("y")
plt.title("Kondensator")














