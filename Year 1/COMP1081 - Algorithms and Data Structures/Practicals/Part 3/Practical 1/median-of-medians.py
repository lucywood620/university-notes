import random
import math
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def median_of_medians(A,i):
    if len(A)<=5:
        A.sort()
        return A[i]
    divide=list(chunks(A, math.ceil(len(A))))
    print(divide)


for i in range(10):
    # A=range(50000)
    A=[i for i in range (50000)]
    random.shuffle(A)
    i=random.randint(0,50000-1)
    x=median_of_medians(A,i)
    if x==i:
        print('i=%d OK' % i)
    else:
        print('i=%d something is wrong' %i)

print(chunks([i for i in range (23)],5))