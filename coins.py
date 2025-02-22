'''coins=[1,2,5,10]
n=int(input("Enter the amount"))
d={}
i=3
while n>0:
    div=n//coins[i]
    #d.setdefault(coins[i],div)
    d[coins[i]]=div
    n=n%coins[i]
    i=i-1
print(d)'''

x = 5
f = lambda x: 1 + 2
print(f(x))