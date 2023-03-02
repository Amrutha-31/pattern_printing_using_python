n=int(input())
for i in range(1,n+1):
    if i==n:
        print("*"*n)
    elif i>=1 and i<n:
        print("*"+' '*(n-2)+"*")