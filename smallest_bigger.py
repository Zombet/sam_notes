import itertools

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
    print("".join(list(permutations[a])))