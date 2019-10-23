import math
coord=input("What are the coordinates?")
coord=coord.split(",")
x=float(coord[0])
y=float(coord[1])

if math.sqrt(x**2+y**2)<=8:
    print("Hit")
else:
    print("Miss")