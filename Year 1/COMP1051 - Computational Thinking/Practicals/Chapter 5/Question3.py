import math
def heron(n,error,x0):
    i2=x0
    count=0
    while(True):
        count+=1
        i1=0.5*(i2+(n/i2))
        print(i1)
        i2=0.5*(i1+(n/i1))
        print(i2)
        print(i2-i1)
        if(abs(i2-i1)<error):
            break
    print(i2)
    print(count)
heron(math.sqrt(2),0.000000000000001,24)
