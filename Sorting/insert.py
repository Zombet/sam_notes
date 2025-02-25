def insert(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key.lower() < arr[j].lower():
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

arr=input("Enetr list of strings to be sorted : ").split()
insert(arr)
print(arr)

'''import sys
inp=sys.argv[1:]
print(inp)'''