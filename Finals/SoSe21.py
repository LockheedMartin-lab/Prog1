"""
Created on Sat Jul 01 15:30:47 2023
@author: LockheedMartin
# SoSe 21
"""
#janky import
import math as math

#defining all the shit I can
g = 9.81
h = 10
t_start = 0
"""
#function def
def x(t):
    vx0 * t
    
def y(t):
    h+vy0 * t - .5 * g*t**2
"""

#lazy way of saying give me the right fcking angle...
angle = -50
while angle<10 or angle>35:
    angle=int(input("Geben Sie den Winkel phi in Grad ein (10<=phi<=35): "))
    
    if angle<10 or angle>35:
        print("Falsche Eingabe fuer phi: 10<=phi<=35")
    else:
        break


vx0 = 5*math.cos(angle)
vy0 = 5*math.sin(angle)

t_end = vy0/g + ( (vy0/g)**2 + 2*h/g )**.5

delta = t_end/30
x_max = 0

#placeholders:
p1 = "t"
p2 = "x(t)"
p3 = "y(t)"

print(f"{p1:^10}{p2:^10}{p3:^10}")
print("- - - - - - - - - - - - - - - - - -")
while t_start<t_end:
    
    x = vx0 * t_start
    y = h+vy0 * t_start - .5 * g*t_start**2
    
    if x<x_max:
        x_max = x
        t_max = t_start
        y_max = y
    
    print(f"{t_start:^10.4}{x:^10.4}{y:^10.4}")
    t_start+=delta
    
print(f"Die maximale Hoehe {x_max:.2} wird nach {t_max:.2} Sekunden erreicht")
print("Die zugehoerigen Koordinaten sind xmax= {x_max:.2} und ymax= {y_max:.2}")