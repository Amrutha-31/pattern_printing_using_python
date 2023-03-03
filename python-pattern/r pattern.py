n=int(input())
for i in range(1,n+1):
    if i==1:
        print("*"*n)
    elif i>(n//2) and i<n+1:
        print("*"+' '*(1+i)+"*")
    elif i==(n//2):
        print("*"*n)
    elif i<=(n//2):
        print("*"+' '*(n-2)+"*")
    