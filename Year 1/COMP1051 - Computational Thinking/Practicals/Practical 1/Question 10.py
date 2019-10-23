a_list = ['piae', 'mash', 7, 4.3, 'aeel']
a_string = 'pass'
sum = a_list[2] + a_list[3]
# if sum % 1 == 0:
#    print("Sum is an integer")
#
# if len(a_list) > len(a_string):
#    print('Longer')
#
# print(a_string[1])
# print('q' in a_string)

for item in a_list:
    print(item)
    if str(item).find('a') != -1:
        print("Found a in " + item)
