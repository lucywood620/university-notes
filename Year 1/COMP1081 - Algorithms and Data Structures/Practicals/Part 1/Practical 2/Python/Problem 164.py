sum = 0
count = 0
tempok = 0
number = (10 ** 19)
while len(str(number)) == 20:
    number += 1
    tempok = 0

    stringnum = str(number)
    for i in range(0, 17):
        sum = int(stringnum[i]) + int(stringnum[i + 1]) + int(stringnum[i + 2])
        if sum <= 9:
            tempok = 1
        else:
            tempok = 0
            break
    if tempok == 1:
        count += 1

    number += 1
print(count)
