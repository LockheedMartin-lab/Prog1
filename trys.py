#%% try T5 A4 

soll = int(input("Sollwert in Ohm: "))

werte = [10, 47, 100, 150, 220, 330, 470, 1000, 1500, 2200, 4700, 10000, 22000, 27000, 33000, 47000, 100000, 220000, 470000, 1000000]

#diff = 1000000
diff = max(werte)
anz = len(werte)
r1no = 0
r2no = 0

for r1 in range(0, anz):
    for r2 in range(0, anz):
        #unt = werte[r1] + werte[r2] - soll
        print(f"{r1}*{r2}/{r1}+{r2}")
"""        rges=(r1*r2)/(r1+r2)
        
        posrges = abs(rges)
        
        
        if posrges < diff:
            diff = posrges
            r1no = r1
            r2no = r2
            
r1value = werte[r1no]
r2value = werte[r2no]
r_total = r1value + r2value

print(f"Resistor 1: {r1value} Ohm")
print(f"Resistor 2: {r2value} Ohm")
print(f"Total Resistance: {r_total} Ohm")
print(f"Difference in Ohm: {diff}")
print(f"Difference in %: {diff / soll * 100}%")"""

