def compare(x, y):
    count = 0
    for i in range(0, len(x)):
        count += 1
        if x[i] != y[i]:
            print(count)
            return False
    print(count)
    return True



print(compare("Hello","Hello"))