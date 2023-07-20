#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:50:32 2023

@author: LockheedMartin
"""


#%%check Variante input Def. Aufbau -> Funktion, Name, min, max
def input_int(msg, i_min, i_max):
    i=int(input(msg))
    while i<i_min or i>i_max:
        print("Please korrect value")
        i=int(input(msg))
    return i

# x2=inp.input_int("Variante B: ", 1, 10)

#%%prime Numbers: True/False
def check_prime(x):
    if x < 2:  # Numbers less than 2 are not prime
        return False
    for i in range(2, x):
        if x % i == 0:  # If x is divisible by any number from 2 to x-1, it is not prime
            return False
    return True

#p = check_prime(19)
#print(f"19 --> {p}")

#%% resistor check:
    
def resistor_solo(x):
    werte=[10, 47, 100, 150, 220, 330, 470, 1000, 1500, 2200, 4700, 10000, 22000, 27000, 33000, 47000, 100000, 220000, 470000, 1000000]

    anz=len(werte)
    
    diff=[]
    l=0
    for i in range(0, anz):
        unt=werte[i]-x
        posunt=abs(unt)
        diff.append(posunt)
        l=l+1
        
        #findng the index of the lowest value
        z=diff.index(min(diff))
        zw=min(diff)
        zwpr=zw*100/x
        db=werte[z]
        
    print(f"Lowest resistor is {db}")
    print(f"Difference: {zw} Ohm ({zwpr:.3}%)")
        
        
        
        
#%% resistor chain try

def resistor_chain(x):
    werte = [10, 47, 100, 150, 220, 330, 470, 1000, 1500, 2200, 4700, 10000, 22000, 27000, 33000, 47000, 100000, 220000, 470000, 1000000]

    diff = 1000000
    diff = max(werte)
    anz = len(werte)
    r1no = 0
    r2no = 0

    for r1 in range(0, anz):
        for r2 in range(0, anz):
            unt = werte[r1] + werte[r2] - x
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
    print(f"Difference in %: {diff / x * 100}%")
    
    
#%% parallel resistor def

def paralell_resistor(x):
    
    werte = [10, 47, 100, 150, 220, 330, 470, 1000, 1500, 2200, 4700, 10000, 22000, 27000, 33000, 47000, 100000, 220000, 470000, 1000000]
    
    diff = 1000000
    diff = max(werte)
    anz = len(werte)
    r1no = 0
    r2no = 0
    
    for r1 in range(0, anz):
        for r2 in range(0, anz):
            rges=(werte[r1]*werte[r2])/(werte[r1]+werte[r2])
            rdiff=rges-x
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
    print(f"Difference: {diff:.2f} Ohm ({diff / x * 100:.2f}%)")


