friend_list=[['Michael','Holly'],['Iain','Sam'],['Holly','r2d2'],['Magnus','r2d2'],['Daniel','Iain'],['Jim','Rob'],['Iain','Michael'],['a','b']]
link_list=[]
fine=1
i=0
while True:
    if fine == 0:
        i=i+1
    if i==len(link_list):
        link_list.append([])
    if len(friend_list)==0:
        break
    fine=0
    for item in range(0,len(friend_list)):
        if len(link_list[i])==0 and (friend_list[item][0] and friend_list[item][1] not in link_list[i-1]):
            link_list[i].append(friend_list[item][0])
            link_list[i].append(friend_list[item][1])
            del friend_list[item]
            continue


        try:
            if friend_list[item][0] in link_list[i] and friend_list[item][1] not in link_list[i]:
                link_list[i].append(friend_list[item][1])
                del friend_list[item]
                fine=1
                break
        except IndexError:
            print(item)
            print(friend_list)
            print(link_list)
            # import sys
            # sys.exit()
            continue
        if friend_list[item][1] in link_list[i] and friend_list[item][0] not in link_list[i]:
            link_list[i].append(friend_list[item][0])
            del friend_list[item]
            fine=1
            break



print(link_list)