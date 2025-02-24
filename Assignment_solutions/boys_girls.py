t=int(input("Enter number of test cases : "))
for i in range (t):
    n=int(input("Enter number of boys or girls : "))
    bh=list(map(int,input("Enter height of boys : ").split()))
    gh=list(map(int,input("Enter height of girls : ").split()))
    fl=sorted(gh+bh)
    bmatch,gmatch=0,0
    for j in range (0,len(fl),2):
        if fl[j] in bh:
            
            bmatch +=1
        else:
            
            gmatch+=1
    if bmatch==n or gmatch==n:
        print("Yes")
    else:
        print("No")
