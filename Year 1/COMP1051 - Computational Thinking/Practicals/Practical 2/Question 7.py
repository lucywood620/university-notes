list = input("Input a list")
list=list.replace("[","")
list=list.replace("]","")
list=list.split(",")
for item in list:
    if 65<=ord(item[0])<=77:
        print(item)