import math
def points (x1,y1,x2,y2):
    length=math.sqrt((x2-x1)**2+(y2-y1)**2)
    gradient=(y2-y1)/(x2-x1)
    intercept=y2-gradient*x2


    return "Length is"+str(length)+"Equation is: y="+str(gradient)+"x+"+str(intercept)

print(points(1,2,3,4))
