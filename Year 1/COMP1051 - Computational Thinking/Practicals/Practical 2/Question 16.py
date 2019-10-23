import string
def partition(list2):
    for item in list2:
        item=item[0]
    print(list2)

    lower=set(string.ascii_lowercase[:12])
    upper=set(string.ascii_lowercase[12:])
    lowerc=set(upper) & set(list2)
    return lowerc
print(partition(['hello','world']))