'''import itertools

def generate_permutations(arr):
    return sorted(list(itertools.permutations(arr)))

n=input("Enter a number : ")
arr = []
for i in n:
    arr.append(i)


permutations = generate_permutations(arr)

a=permutations.index(tuple(arr))+1
if a>=len(permutations):
    print("Not possible")
else:
    print("".join(list(permutations[a])))'''

'''i = 250
while len(str(i)) > 72: 
    i *= 2
else: 
    i //= 2
print(i)'''

lst = [[c for c in range(r)] for r in range(3)]
for x in lst:
    for y in x:
        if y < 2:
            print('*', end='')
