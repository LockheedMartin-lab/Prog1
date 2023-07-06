#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:30:47 2023

@author: LockheedMartin



Anotation (only in this file): 
    #%%#: Finished
    #%% : something's wrong, baybe dk what though 

"""

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



#%%# T6 A1 working but weird af
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
    








 





#%% T6 A1 broken (it's a lost cause, just figuring out wtf was intended is enough work :P)


#t in sec
t_start = 0
t_end = 1 #changed later on
t_delta = .05 #increment

#other specs
R = 13.5*10**3
F = 35.1*10**6
g = 9.81
c = 340
stopcalcperc = 95 #stop calc at fuel %


#function try
#a: beschl
#

import matplotlib.pyplot as plt

#Index indicates start loadout
m_start = 2.75*10**6
m_stage1perc = 72.2 #weight end stage
m_stage1 = m_start - (m_start*m_stage1perc/100)
m_end = m_stage1 * m_stage1perc / 100


#Calc of calc duration
t = m_start/R
t_end = t * m_stage1perc / 100

#create list
t_values = []
v_values = []


#first run values
m = m_start
v = 0

while t <= t_end: 
    
    #update list (to include t&v=0)
    t_values.append()
    v_values.append()
    
    
    m = m - R * t_delta
    a = (F/m) - g
    v = v + t_delta * a
    
    
    print(f" t = {t:.2f} s, v = {v:.2f}")
    
    
    t=t+t_delta
    t_values.append(t)
    v_values.append(v)


plt.plot(t_values,v_values,"r--")
plt.grid(True)
plt.show()




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


#%%# T6 A2

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






#%%# T6 A2 2. solution

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






#%% rocket try 10 aka hopefully last try :P (it wasn't btw)

#imports
import matplotlib.pyplot as plt

print("Test1 :)")
#other specs
R = 13.5*10**3 #Fuel usage
F = 35.1*10**6 #force outwards
g = 9.81 #legendary G
c = 340 #speed of sound in m/s
stopcalcperc = 5 #in %

print("Test2 :)")
#weight num
fuel_weight_perc = 72.7
stop_calc_weight_perc = 100 - 95
liftof_weight = 2.75 *10**6
fuel_weight = liftof_weight * fuel_weight_perc / 100
stop_calc_weight = fuel_weight * stop_calc_weight_perc / 100

print("Test3 :)")
#create list
t_values = [] #x-Axis
v_values = [] #y-Axis

print("Test4 :)")
#first run values -> adjusting (hopefully by them selfes :P)
v = 0
t = 0
m = liftof_weight
t_delta = 0.05
current_weight = fuel_weight = m

print("Test5 :)")

while current_weight > stop_calc_weight:
    m = m - R * t_delta
    a = F / m - g
    v = v + t_delta * a

    print(f"m: {m}, a: {a}, v: {v}")
    t_values.append(t)
    v_values.append(v)

    t+=t_delta
    print("Testxxx :)")


plt.plot(t_values,v_values,"r--")
plt.grid(True)
plt.show()

print("Test6 :)")

"""
#t in sec idk if I need it tbh
t_start = 0 #time start
t_end = 1 #changed later on
t_delta = .05 #increment



#Calc of calc duration
t = m_start/R
t_end = t * m_stage1perc / 100
#t_calcend = 


#calc m: (in while)
#m_start = m_start - R * t
"""


#%% try  T6 A3 not finished

import math as math

y = int(input("value for y: "))
x = int(input("value for x: "))

increment_y = .1
y_start = 0
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
    var = var_0 + delta_var
    count.append(var)
    u+=1

print(f"x|y   |{count[0]:6.1f}{count[1]:6.1f}{count[2]:6.1f}{count[3]:6.1f}{count[4]:6.1f}{count[5]:6.1f}{count[6]:6.1f}{count[7]:6.1f}")

###

print("x|y  |  0.0    0.1    0.2    0.3    0.4    0.5    0.6    0.7    0.8  ")

y_value = []
x_value = []

while x_start < x_end:
    

    
    while y_start < y_end:
        
        f = (e**(-(x**2 + y**2)))/(1 + x**2 + y**2)**.5
        y_value.append(f)
        x_value.append(x)
        
        y = y + increment_y
        
        print(f"{y_value[0]:6.3f}{x_value[0]:6.3f}{x_value[1]:6.3f}{x_value[2]:6.3f}{x_value[3]:6.3f}{x_value[4]:6.3f}{x_value[5]:6.3f}{x_value[6]:6.3f}{x_value[7]:6.3f}")


    y_value = []
    x_value = []
    x_start = x_start + increment_x
    




#%% try2  T6 A3 not finished

import math as math

y = int(input("value for y: "))
x = int(input("value for x: "))

increment_y = .1
y_start = 0
y_end = .8

increment_x = .2
x_start = 0
x_end = 1.4

#Important info:
    #Cell size 6 & .*** dec


e = math.e #def of e with math 

#f = (e**(-(x**2 + y**2)))/(1 + x**2 + y**2)**.5

print("x|y  |  0.0    0.1    0.2    0.3    0.4    0.5    0.6    0.7    0.8  ")

y_value = []
x_value = []

while x_start < x_end:
    

    
    while y_start < y_end:
        
        f = (e**(-(x**2 + y**2)))/(1 + x**2 + y**2)**.5
        y_value.append(f)
        x_value.append(x)
        
        y = y + increment_y
        
        print(f"{y_value[0]:6.3f}{x_value[0]:6.3f}{x_value[1]:6.3f}{x_value[2]:6.3f}{x_value[3]:6.3f}{x_value[4]:6.3f}{x_value[5]:6.3f}{x_value[6]:6.3f}{x_value[7]:6.3f}{x_value[8]:6.3f}")


    y_value = []
    x_value = []
    x_start = x_start + increment_x
    






#%% T6 A3 not finished

import math

y = 0
x = 0

increment_y = 0.1
y_start = 0
y_end = 0.8

increment_x = 0.2
x_start = 0
x_end = 1.4

e = math.e

print("x|y  |  0.0    0.1    0.2    0.3    0.4    0.5    0.6    0.7    0.8  ")

while x_start <= x_end:
    y_start = 0
    
    while y_start <= y_end:
        f = (e**(-(x**2 + y**2))) / (1 + x**2 + y**2)**0.5
        print(f"{x:6.3f}{y:6.3f}{f:6.3f}", end=" ")
        y_start += increment_y
        y = round(y + increment_y, 1)
    
    print()
    x_start += increment_x
    x = round(x + increment_x, 1)
    y = 0



