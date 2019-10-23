x = 'hello'
y = 'goodbye'
if len(x) == len(y):
    print("Same Length")
if x[2] == y[2]:
    print("The 3rd Character is the same")
for i in range(0, len(x)):
    if x[i] == x[i - 1]:
        print('Two consecutive ls in x')
for i in range(0, len(y)):
    if y[i] == y[i - 1]:
        print('Two consecutive ls in y')
if y.find(x[0])==-1:
    print("First letter of x not in y")
