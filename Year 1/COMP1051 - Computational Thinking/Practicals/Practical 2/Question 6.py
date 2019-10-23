list = input("Input a list")
list=list.replace("[","")
list=list.replace("]","")
list=list.split(",")
if 'Secret' in list:
    list.remove("Secret")
print(list)