#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:30:47 2023

@author: LockheedMartin
"""


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


#%% Special 2 (p14):

soll = 0

try:
    soll=int(input("Sollwert in Ohm: "))
    
    werte = [10, 47, 100, 150, 220, 330, 470, 1000, 1500, 2200, 4700, 10000, 22000, 27000, 33000, 47000, 100000, 220000, 470000, 1000000]

    #diff = 1000000
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
    
except ValueError:
    print("Check value!")


#%%Special 3 (p14):
    

soll = 0

try:
    
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
    
    print(" ")
    print("Single: ")
    print(f"Lowest resistor is {db}")
    print(f"Difference: {zw} Ohm ({zwpr:.3}%)")
    print(" ")
    
    #parallel     

    #diffp = 1000000
    diffp = max(werte)
    anz = len(werte)
    r1no = 0
    r2no = 0

    for r1 in range(0, anz):
        for r2 in range(0, anz):
            rges=(werte[r1]*werte[r2])/(werte[r1]+werte[r2])
            rdiffp=rges-soll
            posrdiffp = abs(rdiffp)
            
            if posrdiffp < diffp:
                diffp = posrdiffp
                r1no = r1
                r2no = r2
                srges=rges



    r1value = werte[r1no]
    r2value = werte[r2no]

    print("Parallel: ")
    print(f"best paralell resistor combo: {r1value} and {r2value} Ohm.")
    print(f"Total Resistance: {srges:.2f} Ohm")
    print(f"Difference: {diffp:.2f} Ohm ({diffp / soll * 100:.2f}%)")
    print(" ")
    
    
    #Chain

    #diffc = 1000000
    diffc = max(werte)
    anz = len(werte)
    r1no = 0
    r2no = 0

    for r1 in range(0, anz):
        for r2 in range(0, anz):
            unt = werte[r1] + werte[r2] - soll
            posunt = abs(unt)
            
            if posunt < diffc:
                diffc = posunt
                r1no = r1
                r2no = r2
                
    r1value = werte[r1no]
    r2value = werte[r2no]
    r_total = r1value + r2value

    print("Chain:")
    print(f"Resistor 1: {r1value} Ohm")
    print(f"Resistor 2: {r2value} Ohm")
    print(f"Total Resistance: {r_total} Ohm")
    print(f"Difference in Ohm: {diffc}")
    print(f"Difference in %: {diffc / soll * 100:.2}%")
    print(" ")   
    
    if diffc<diffp and diffc<zw:
        bestres="chain"
    elif diffp<diffc and diffp<zw:
        bestres="paralell"
    else:
        bestres="single"
    
    print(f"Min deviation is {min(diffc, diffp, zw):.2} as {bestres}")
    
    
except ValueError:
    print("Check value!")



#%%Special 4 (p14):


soll = 0

try:
    
    werte=[10, 47, 100, 150, 220, 330, 470, 1000, 1500, 2200, 4700, 10000, 22000, 27000, 33000, 47000, 100000, 220000, 470000, 1000000]

    soll=int(input("Sollwert in Ohm: "))
    
    
    while soll>0:
        #Besten Einzelwiderstand ermitteln (geringste Abweichng):
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
        
        print(" ")
        print("Single: ")
        print(f"Lowest resistor is {db}")
        print(f"Difference: {zw} Ohm ({zwpr:.3}%)")
        print(" ")
        
        #parallel     

        #diffp = 1000000
        diffp = max(werte)
        anz = len(werte)
        r1no = 0
        r2no = 0

        for r1 in range(0, anz):
            for r2 in range(0, anz):
                rges=(werte[r1]*werte[r2])/(werte[r1]+werte[r2])
                rdiffp=rges-soll
                posrdiffp = abs(rdiffp)
                
                if posrdiffp < diffp:
                    diffp = posrdiffp
                    r1no = r1
                    r2no = r2
                    srges=rges



        r1value = werte[r1no]
        r2value = werte[r2no]

        print("Parallel: ")
        print(f"best paralell resistor combo: {r1value} and {r2value} Ohm.")
        print(f"Total Resistance: {srges:.2f} Ohm")
        print(f"Difference: {diffp:.2f} Ohm ({diffp / soll * 100:.2f}%)")
        print(" ")
        
        
        #Chain

        #diffc = 1000000
        diffc = max(werte)
        anz = len(werte)
        r1no = 0
        r2no = 0

        for r1 in range(0, anz):
            for r2 in range(0, anz):
                unt = werte[r1] + werte[r2] - soll
                posunt = abs(unt)
                
                if posunt < diffc:
                    diffc = posunt
                    r1no = r1
                    r2no = r2
                    
        r1value = werte[r1no]
        r2value = werte[r2no]
        r_total = r1value + r2value

        print("Chain:")
        print(f"Resistor 1: {r1value} Ohm")
        print(f"Resistor 2: {r2value} Ohm")
        print(f"Total Resistance: {r_total} Ohm")
        print(f"Difference in Ohm: {diffc}")
        print(f"Difference in %: {diffc / soll * 100:.2}%")
        print(" ")   
        
        if diffc<diffp and diffc<zw:
            bestres="chain"
        elif diffp<diffc and diffp<zw:
            bestres="paralell"
        else:
            bestres="single"
        
        print(f"Min deviation is {min(diffc, diffp, zw):.2} as {bestres}")
        
        
        soll=int(input("wanna do another? type in next value:  "))

   



 
except ValueError:
    print("Check value!")
    
        
#%% Special 999:
    
soll = 0

try:
    
    werte=[10, 47, 100, 150, 220, 330, 470, 1000, 1500, 2200, 4700, 10000, 22000, 27000, 33000, 47000, 100000, 220000, 470000, 1000000]

    soll=int(input("Sollwert in Ohm: "))
    
    
    while soll>0:
        #Besten Einzelwiderstand ermitteln (geringste Abweichng):
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
        
        print(" ")
        print("Single: ")
        print(f"Lowest resistor is {db}")
        print(f"Difference: {zw} Ohm ({zwpr:.3}%)")
        print(" ")
        
        #parallel     

        #diffp = 1000000
        diffp = max(werte)
        anz = len(werte)
        r1no = 0
        r2no = 0

        for r1 in range(0, anz):
            for r2 in range(0, anz):
                rges=(werte[r1]*werte[r2])/(werte[r1]+werte[r2])
                rdiffp=rges-soll
                posrdiffp = abs(rdiffp)
                
                if posrdiffp < diffp:
                    diffp = posrdiffp
                    r1no = r1
                    r2no = r2
                    srges=rges



        r1value = werte[r1no]
        r2value = werte[r2no]

        print("Parallel: ")
        print(f"best paralell resistor combo: {r1value} and {r2value} Ohm.")
        print(f"Total Resistance: {srges:.2f} Ohm")
        print(f"Difference: {diffp:.2f} Ohm ({diffp / soll * 100:.2f}%)")
        print(" ")
        
        
        #Chain
        #diffc = 1000000
        diffc = max(werte)
        anz = len(werte)
        r1no = 0
        r2no = 0

        for r1 in range(0, anz):
            for r2 in range(0, anz):
                unt = werte[r1] + werte[r2] - soll
                posunt = abs(unt)
                
                if posunt < diffc:
                    diffc = posunt
                    r1no = r1
                    r2no = r2
                    
        r1value = werte[r1no]
        r2value = werte[r2no]
        r_total = r1value + r2value

        print("Chain:")
        print(f"Resistor 1: {r1value} Ohm")
        print(f"Resistor 2: {r2value} Ohm")
        print(f"Total Resistance: {r_total} Ohm")
        print(f"Difference in Ohm: {diffc}")
        print(f"Difference in %: {diffc / soll * 100:.2}%")
        print(" ")   
        
        if diffc<diffp and diffc<zw:
            bestres="chain"
        elif diffp<diffc and diffp<zw:
            bestres="paralell"
        else:
            bestres="single"
        
        print(f"Min deviation is {min(diffc, diffp, zw):.2} as {bestres}")
        
        
        #NEW:
        import numpy as np
        import matplotlib.pyplot as plt

        # some example data
        threshold = min(diffc, diffp, zw)
        values = np.array([diffc, diffp, zw])
        x = range(len(values))

        # split it up
        above_threshold = np.maximum(values - threshold, 0)
        below_threshold = np.minimum(values, threshold)

        # and plot it
        fig, ax = plt.subplots()
        ax.bar(x, below_threshold, 0.35, color="g")
        ax.bar(x, above_threshold, 0.35, color="r", bottom=below_threshold)

        # horizontal line indicating the threshold
        ax.plot([0., 4.5], [threshold, threshold], "k--")

        fig.savefig("look-ma_a-threshold-plot.png")
        plt.show() #to show the graph
        
        
        soll=int(input("wanna do another? type in next value:  "))
        

except ValueError:
    print("Check value!")



#%% ADD

import numpy as np
import matplotlib.pyplot as plt

# some example data
threshold = 43.0
values = np.array([30., 87.3, 99.9, 3.33, 50.0])
x = range(len(values))

# split it up
above_threshold = np.maximum(values - threshold, 0)
below_threshold = np.minimum(values, threshold)

# and plot it
fig, ax = plt.subplots()
ax.bar(x, below_threshold, 0.35, color="g")
ax.bar(x, above_threshold, 0.35, color="r",
        bottom=below_threshold)

# horizontal line indicating the threshold
ax.plot([0., 4.5], [threshold, threshold], "k--")

fig.savefig("look-ma_a-threshold-plot.png")

