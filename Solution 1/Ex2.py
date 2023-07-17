#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:30:47 2023

@author: LockheedMartin
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
    
