def cntlsta(lst,k):
    sum=0
    l=[]
    s=0
    i=0
    if k==0:
        return 0
    while i < (len(lst)):
        sum=sum+lst[i]
        l.append(lst[i])
        i=i+1
        if sum==k:
            return l
        if sum>k:
            sum=0
            s=s+1
            i=s
            l=[]

    return None

print(cntlsta([1,2,3,4,15],9))
print(cntlsta([1,2,3,4,115],115))
print(cntlsta([5,8,1,7,4,15],9))
print(cntlsta([],1))
