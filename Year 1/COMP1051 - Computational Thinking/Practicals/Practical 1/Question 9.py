import math
a_list=['pie','mash',7,53,6,'eel',2]
middle=math.ceil(len(a_list)/2)-1
print("Middle index is: "+str(middle))
print("Middle element is: " + str(a_list[middle]))
#for item in a_list:
#    item=str(item)
b_list=[str(i) for i in a_list]
print(b_list)
b_list.sort()
print(b_list)
a_list.append(a_list[0])
del a_list[0]
print(a_list)
