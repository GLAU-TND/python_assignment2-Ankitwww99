def no_dec(lst):
    c=0
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            c=c+1
        if c>1:
            return False
    return True

lst=[10, 5, 1]
print(no_dec(lst))
