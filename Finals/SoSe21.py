"""
Created on Sat Jul 01 15:30:47 2023
@author: LockheedMartin
# WiSe 22/23
"""
#%% A1 -> TM 

import math as m

Winkel = []
Kräfte = []
kx = []
ky = []

k = int(input("Kraft / N: "))
while k > 0: 
    Kräfte.append(k)
    w = int(input("Winkel / Grad: "))
    kx.append(k*m.cos(m.radians(w)))
    ky.append(k*m.sin(m.radians(w)))
    k = int(input("Kraft / N: "))
    Winkel.append(w) 
else: 
    print("Es wurden keine Kräfte eingegeben.")

i = len(Kräfte)
j = 1
while i > 0: 
    print(f"{j:>4}:", end="")
    l = Kräfte[j-1]
    print(f"{l:>8.3f}N", end="")
    h = Winkel[j-1]
    print(f"{h:>8}°", end="")
    print()
    j+=1
    i-=1

kxg = sum(kx)
kyg = sum(ky)
kg = m.sqrt(kxg**2 + kyg**2) 
print(f"{kg:.3f}")
wgx = m.acos(kxg/kg)
wg = m.degrees(wgx)
print(f"{wg:.3f}")


#%% A3 -> find x in input

def find_first(s, ch):
    anz = len(s)
    pos = -1
    for i in range(0, anz):
        if ch in s:
            pos = s.index(ch) + 1
            break
    return pos

s = input("Zeichenkette eingeben: ")
ch = "x"
pos = find_first(s, ch)

if pos == -1:
    print(f"Das Zeichen {ch} wurde nicht gefunden")
    
else:
    print(f"Das Zeichen {ch} wurde an Position {pos} gefunden.")



#%% A4 -> plot red&blue

import matplotlib.pyplot as plt
ys = []
xs = []
A = []
x = -1

while x <= 2:
    y = 3*x**3 - 5*x**2 +1
    Ay = 9* x **2 - 10*x
    ys.append(y)
    A.append(Ay)
    xs.append(x)
    x+= .1
    
plt.plot(xs, ys, "r")
plt.plot(xs, A, "b")
plt.grid(True)
plt.show() 

