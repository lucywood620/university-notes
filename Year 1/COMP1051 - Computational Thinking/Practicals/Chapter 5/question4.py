import itertools
def subsetsum(list):
    numbers = list
    result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i)]
    print(result)
#subsetsum(["A","B","C","D"])
print([x for x in itertools.permutations('ABCD')])