"""
Created on Mon Jul 17 10:25:20 2023

@author: User1
"""


#%% A1: 

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
