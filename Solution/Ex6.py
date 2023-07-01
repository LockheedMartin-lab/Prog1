#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:30:47 2023

@author: LockheedMartin
"""

#%% ADD nice plot very short

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



#%% T6 A1
"""
Geschwindingkeit einer Saturn-V-Rakete 
waehrend der ersten Stufe
y=m*x+t
x: Zeit
y: Beschlaeunigung


start: t&v 0
m(t) &v(t) known: 
"""
"""

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
""" 
# moved into while

#m = m - R * t_delta
#a = (F/m)-g
#v = v(t)+t_delta * a
"""
import math.plot as plt

#Index indicates start loadout
m_start = 2.75*10**6
m_stage1perc = 72.2 #weight end stage
m_stage1 = m_start - (m_start*m_stage1perc/100)
m_end = m_stage1 * m_stage1perc / 100


#Calc of calc duration
t = m_start/R
t_end = t * m_stage1perc / 100
#t_calcend = 


#calc m: (in while)
#m_start = m_start - R * t

#create list
#t_values = []
#v_values = []


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
    
    
    print(f" t = {t:.2f} s, v = {v:.2f}')
    
    
    t=t+t_delta
    t_values.append(t)
    v_values.append(v)


plt.plot(t_values,y_values,"r--"")
plt.grid(True)
plt.show()

"""


#%% plot, yes another one

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


#%% try      Rocket 2.0










#%% T6 A2 works, but weird plot

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

x_values_a1 = []
y_values_a1 = []

x_values_a2 = []
y_values_a2 = []

x_values_a3 = []
y_values_a3 = []

for a0 in range(0,len(short)):
    #List creation
    

    while x < 10:
        vx0 = v0 * math.cos(math.radians(a0))
        vy0 = v0 * math.sin(math.radians(a0))
        y = (-g / 2) * (x / vx0) ** 2 + vy0 * (x / vx0)

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
            

        x += delta
    
    x = 0
    i = i+1

ax.plot(x_values_a1, y_values_a1, label="a{}".format(a0))
ax.plot(x_values_a2, y_values_a2, label="a{}".format(a0))
ax.plot(x_values_a3, y_values_a3, label="a{}".format(a0))
    
ax.grid(True)
ax.set_xlabel("length in m")
ax.set_ylabel("height in m")
ax.set_title("Sad decreasing function")
ax.legend()

plt.show()




#%% try  T6 A3

import math as math

y = int(input("value for y: "))
x = int(input("value for x: "))

delta_y = .1
y_start = 0
y_end = .8

inter

e = math.e #def of e with math 

f = (e**(-(x**2 + y**2)))/(1 + x**2 + y**2)**.5






