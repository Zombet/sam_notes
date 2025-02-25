arr=[int(ele) for ele in input().split()]
def quic(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    s=[i for i in arr[:-1] if i < pivot]
    b=[j for j in arr[:-1] if j > pivot]
    return quic(s)+[pivot]+quic(b)
print(quic(arr))