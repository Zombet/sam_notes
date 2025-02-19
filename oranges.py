def quicksort(arr):
    if len(arr) <= 1: 
        return arr
    else:
        pivot = arr[-1] 
        less_than_pivot = [x for x in arr[0:-1] if x <= pivot]  # Elements less than pivot
        greater_than_pivot = [x for x in arr[0:-1] if x > pivot]  # Elements greater than pivot
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)  # Recursively sort and combine

n = int(input("Enter number of oranges : "))
d = input("Enter the diameters: ").split()
key=d[-1]
d = quicksort(d)

print("Sorted Diameters:",d)

low=0
high=len(d)-1
while(low<=high):
    mid=(low+high)//2
    if d[mid]==key:
        print("Oranges to be eaten by her children : ")
        for k in range (mid):
            
            print(d[k],end=' ')
        print()
        print("Oranges to be sold in market : ")
        for l in range (mid+1,n):
            
            print(d[l],end=' ')
        break
    elif key<d[mid]:
        high=mid-1
    else:
        low=mid+1


