"""
Created on Sun Jul 16 16:46:51 2023

@author: User2

"""
#%% Aufgabe 1

from math import *
m_start = 2.75e6 #rakede jesamt
m_min_treib = m_start*0.727*0.05 # 
m_nutz = m_start*(1-0.727)


r = 13.5e3
f_schub = 35.1e6
g = 9.81

delta_t = 0.05
c = 340

v = [0]
a = []

t_schall = None
i, t = 1, delta_t
m_aktuell = m_start
while m_aktuell - m_nutz >= m_min_treib:
    
        a.append(f_schub / m_aktuell - g)
        v.append(v[i-1] + delta_t * a[i-1])
        
        if v[-1] >= c and t_schall == None:
            t_schall = t
            
        # korrektur des m_aktuell
        m_aktuell = m_aktuell - r * delta_t
        i += 1
        t += delta_t
        
#Ausgabe
for v_aktuell in v:
        print(f"t = {t:.2f} s, v = {v_aktuell:.3f} m/s")
        t+= delta_t


#%% Aufgabe 2
import math as m
import matplotlib.pyplot as plt


v0 = 10  # m/s
g = 9.81  # m/s^2

def y(x,a):
    vx0 = v0 * m.cos(m.radians(a)) # rechnungen definieren 
    vy0 = v0 * m.sin(m.radians(a))
    
    return -0.5*g*(x/vx0)**2+vy0*(x/vx0) # allgemeine berechnung für die würfe definiereen

# Hauptprogramm

x = []
y20 = []
y40 = []
y60 = []

x_akt = 0

while x_akt < 10:
    x.append(x_akt)
    y20.append(y(x_akt, 20)) # y(x_akt, 20) -> funktion 
    y40.append(y(x_akt, 40))
    y60.append(y(x_akt, 60))
    
    x_akt+=0.05             # setzt den berechnungsschritt    
    
    
plt.plot(x,y20, 'r')
plt.plot(x,y40, 'b')
plt.plot(x,y60, 'k')
plt.grid(True)

plt.plot()
plt.show()


#%% Aufgabe 3

import math as m 

def f(x,y):
    return m.exp(-(x**2+y**2))/m.sqrt(1+x**2+y**2)

# Hauptprogramm
#ycoll = []
#for y in range(9):  # range 9 -> 9 zeilen nach rechts 
#   ycoll.append(y/10)  # 1/10 ... 0.1
    
ycoll = []
y = 0
while y <= 0.8:
    ycoll.append(y)
    y+=.1           # schrittweite soll 0.1 sein deshalb y + .1
    
ycoll = [y/10 for y in range(9)]
xcoll = [0+i*.4 for i in range(8)] # range 8 -> 8 spalten

#erste Zeile
print('x/y   ', end='')
for i in ycoll:
    print(f' {i:^4.1f}', end='')
print()

for x in xcoll:
    print(f'{x:^.1f}/', end='') # end='' unterdrückt den zeilenumbruch
    for y in ycoll:
        z = f(x,y)
        print(f' {z:^.3f}', end='') # nimmt sich immer den wert x und rechnet y dazu aus
                                    # funktion aus der es berechnet wird, ist seperat in z abgespeichert
                                    # wenn man z printed wird die funktion für jedes x und y neu berechnet
        #print(f' {f(x,y):^.3f}', end='')
    print()


#%% Aufgabe 4

from itertools import count


file = open("C:/Users/alice/Desktop/data.txt","r")

for line in file:
    print(line.upper(), end="")


def line_count (name): # name is einfach ein platzhalter für des was unten reinkommt
   with open(name) as myfile:
     total_lines = sum(1 for line in myfile)
   print("---> Anzahl Zeilen: ", total_lines)
   return 

line_count("C:/Users/alice/Desktop/data.txt") 

def int_count (ziffern):
    with open(ziffern) as myfile:
        total_zahlen = sum(1 for int in myfile)
    print("---> Anzahl Ziffern: ", total_zahlen)
    return

int_count ("C:/Users/alice/Desktop/data.txt")
#führ die funktion für die variable/dingi aus was in der klammer steht
    
            
            
file.close()

    
    
    
    