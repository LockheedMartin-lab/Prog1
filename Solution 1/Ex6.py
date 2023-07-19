#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:30:47 2023

@author: LockheedMartin

Anotation (only in this file): 
    #%%#: Finished
    #%% : something's wrong, baybe dk what though 

"""

#%%# plot, yes another one

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

th = np.linspace(0, 2*np.pi, 128)


def demo(sty):
    mpl.style.use(sty)
    fig, ax = plt.subplots(figsize=(3, 3))

    ax.set_title('style: {!r}'.format(sty), color='C0')

    ax.plot(th, np.cos(th), 'C1', label='C1')
    ax.plot(th, np.sin(th), 'C2', label='C2')
    ax.legend()


demo('default')
demo('seaborn-v0_8')


#%%# ADD nice plot very short

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




#%%# T6 A1 -> rocket  


#%%# T6 A1 -> rocket  working but weird af
m_anfang = 2.75e6

m_nutz = m_anfang*(1-0.727)
m_min_treib = m_anfang*0.727*0.05

r = 13.5e3
f_schub = 35.1e6
g = 9.81
delta_t = 0.05
c = 340

v = [0]
a = []
t_schall = None

i, t = 1, delta_t 
m_aktuell = m_anfang
while m_aktuell - m_nutz >= m_min_treib:
    
    a.append(f_schub / m_aktuell - g)
    v.append(v[i-1] + delta_t * a[i-1])
    
    if v[-1]>=c and t_schall== None:
        t_schall = t
    
    #korrektur des m_aktuell
    m_aktuell = m_aktuell - r * delta_t
    
    i+=1
    t+= delta_t
    
#Ausgabe

for v_aktuell in v:
    print(f"t = {t:.2f} s, v = {v_aktuell:.3f} m/s")


#%% T6 A1 -> rocket  !!rocket try 10 aka hopefully last try :P (it wasn't btw)

#imports
import matplotlib.pyplot as plt


#other specs
R = 13.5*10**3 #Fuel usage
F = 35.1*10**6 #force
g = 9.81 #legendary G
c = 340 #speed of sound in m/s
stopcalcperc = 5 #in %


#weight num
fuel_weight_perc = 72.7
stop_calc_weight_perc = 100 - 95
liftof_weight = 2.75 *10**6
fuel_weight = liftof_weight * fuel_weight_perc / 100
stop_calc_weight = fuel_weight * stop_calc_weight_perc / 100


#create list
t_values = [] #x-Axis
v_values = [] #y-Axis


#first run values -> adjusting (hopefully by them selfes :P)
v = 0
t = 0
#m = liftof_weight
t_delta = 0.05
current_weight = fuel_weight #= m



while current_weight > stop_calc_weight:
    a = F / current_weight - g
    v = v + t_delta * a
    current_weight = current_weight - R * t_delta

    print(f"m: {current_weight}, t: {t}, v: {v}")
    t_values.append(t)
    v_values.append(v)
    #print(f"t= {t:.2}, v= {v:.3}")
    t+=t_delta
    



plt.plot(t_values,v_values,"r--")
plt.grid(True)
plt.show()

print(f"v end: {v_values[-1]}")


#%%# T6 A2 -> 3x throw

import matplotlib.pyplot as plt
import math as math


delta = 0.05

a1 = 20
a2 = 40
a3 = 60

v0 = 10  # in m/s
g = 9.81  # in m/s^2

short = [a1, a2, a3]

x = 0  # start of the plot
i = 1 
fig, ax = plt.subplots() #no fucking clue what it does, lmk if you do (allowes you to use the ax pallet as far as ik)

#List creation
x_values_a1 = []
y_values_a1 = []

x_values_a2 = []
y_values_a2 = []

x_values_a3 = []
y_values_a3 = []

y=0
for a0 in short:

    while x < 10:
        vx0 = v0 * math.cos(math.radians(a0))
        vy0 = v0 * math.sin(math.radians(a0))
        y = (-g / 2) * (x / vx0)**2 + vy0 * (x / vx0)

        #if's to change the list append
        if i == 1: 
            x_values_a1.append(x)
            y_values_a1.append(y)
            
        elif i == 2:
            x_values_a2.append(x)
            y_values_a2.append(y)

        elif i == 3:
            x_values_a3.append(x)
            y_values_a3.append(y)
            
        else:
            print("error :/")

        x = x + delta
    
    x = 0
    i = i+1

ax.plot(x_values_a1, y_values_a1, label="a1".format(a0)) #ignore the error, it works...
ax.plot(x_values_a2, y_values_a2, label="a2".format(a0))
ax.plot(x_values_a3, y_values_a3, label="a3".format(a0))


#General plot settings
ax.grid(True)
ax.set_xlabel("length in m")
ax.set_ylabel("height in m")
ax.set_title("Sad decreasing function")
ax.legend()
plt.show()






#%%# T6 A2 -> 3x throw  2. solution

import matplotlib.pyplot as plt
import math as math

delta = 0.05

a1 = 20
a2 = 40
a3 = 60

v0 = 10  # in m/s
g = 9.81  # in m/s^2

#short = [a1, a2, a3]

x = 0  # start of the plot
i = 0
fig, ax = plt.subplots() #no fucking clue what it does, lmk if you do (allowes you to use the ax pallet as far as ik)

#List creation
x_values_a1 = []
y_values_a1 = []


y=0


while i<3:
    
    if i == 0:
        p = a1
    elif i == 1:
        p = a2
    else:
        p = a3
            
    while x < 10:
        
        #calc
        vx0 = v0 * math.cos(math.radians(p))
        vy0 = v0 * math.sin(math.radians(p))
        y = (-g / 2) * (x / vx0)**2 + vy0 * (x / vx0)
        
        x_values_a1.append(x) #add to list
        y_values_a1.append(y)
        
        x+=delta
    
    ax.plot(x_values_a1, y_values_a1, label="a" f"{i}".format(p))
    x=0
    x_values_a1 = []
    y_values_a1 = []
    i+=1




#vx0 = v0 * math.cos(math.radians(p))
#vy0 = v0 * math.sin(math.radians(p))


#General plot settings
ax.grid(True)
ax.set_xlabel("length in m")
ax.set_ylabel("height in m")
ax.set_title("Sad decreasing function")
ax.legend()
plt.show()







#%%# T6 A3 -> table  automated scale

import math as math

#y = int(input("value for y: "))
#x = int(input("value for x: "))

increment_y = .1
y_end = .8

increment_x = .2
x_start = 0
x_end = 1.4

#Important info:
    #Cell size 6 & .*** dec


e = math.e #def of e with math 

#f = (e**(-(x**2 + y**2)))/(1 + x**2 + y**2)**.5

###till next 3x #: automated version of first print
u=0
var_0 = 0
delta_var = .1
count= [0]
while u<8:
    var_0 = var_0 + delta_var
    count.append(var_0)
    u+=1
    
lable = "x|y" #so it's centered below, that way you don't have to search for the right amount of spaces below
print(f"{lable:^6}  {count[0]:^6.1f}{count[1]:^6.1f}{count[2]:^6.1f}{count[3]:^6.1f}{count[4]:^6.1f}{count[5]:^6.1f}{count[6]:^6.1f}{count[7]:^6.1f}{count[8]:^6.1f}") #first line and 





y_value = []
x_value = []
x = 0

while x <= x_end:
    y = 0
    
    while y < y_end:
        
        f = (e**(-(x**2 + y**2)))/(1 + x**2 + y**2)**.5
        y_value.append(f)
        x_value.append(x)
        
        y = y + increment_y


    print(f"{x_value[0]:^6.1f}|{y_value[0]:6.3f}{y_value[1]:6.3f}{y_value[2]:6.3f}{y_value[3]:6.3f}{y_value[4]:6.3f}{y_value[5]:6.3f}{y_value[6]:6.3f}{y_value[7]:6.3f}{y_value[8]:6.3f}")

    y_value = []
    x_value = []
    
    x = x + increment_x



#%%# T6 A3 -> table  short and nice solution :)

import math as m

def funktion(x,y): 
    fxy=(m.e**(-(x**2+y**2)))/(m.sqrt(1+x**2+y**2)) 
    return fxy
    
xwerte=[x*0.1 for x in range(0,16,2)] 
ywerte=[y*0.1 for y in range(0,9,1)]

print("x|y", end="") 
for i in ywerte:
    print(f"{i:^6.1f}",end="") 
print()
for l in xwerte: 
    print(f"{l:<4.1f}|",end="") 
    for w in ywerte:
        wert=funktion(l, w)
        print(f"{wert:<6.3f}",end="") 
    print()
x = funktion(0.2, 0.3)
print()
print(f"{x}")



#%% T6 A4 -> line counter  start but idk about the num count, can't test this one
i = 0
file = open("c:/temp/data.txt", "r")
for line in file:
    print(line.upper(), end="")
    i=i+1
    

print(f"Lines: {i}")
file.close()