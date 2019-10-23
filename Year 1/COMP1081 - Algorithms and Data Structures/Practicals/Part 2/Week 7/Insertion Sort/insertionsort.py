import random


list=list(range(5))
random.shuffle(list) # << shuffle before print or assignment
print(list)
list=[5,4,3,2,1]
# In the correct order, this will take 0 comparisons
# In the inverse order, this will take 21 comparisons
# When randomised, this will take a value between the two, the ones with the least swaps needed to sort the list into order running faster

counter=0
for i in range(2,len(list)):
    x=list[i]
    j=i-1
    while j>0 and list[j]>x:
        counter+=1
        list[j+1]=list[j]
        j-=1
    list[j+1]=x
print(list)
print(counter)
