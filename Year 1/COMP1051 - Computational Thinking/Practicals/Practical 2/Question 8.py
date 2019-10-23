integer=int(input("What is the integer n"))
def multiples(m, count):
    for i in range(1,count+1):
        print(i*m)
multiples(integer,4)