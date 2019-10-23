import math
def collision (x1,y1,r2,x2,y2,r2):
    distance=math.sqrt((y2-y1)**2+(x2-x1)**2)
    if distance<(r1+r2):
        return "CRASH!"
