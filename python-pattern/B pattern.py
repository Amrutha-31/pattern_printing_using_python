n=int(input())
for i in range(1,n+1):
    if i==1:
        print("*"*n)
    elif i==n:
        print("*"*n)
    elif i==(n//2):
        print("*"*n)
    else:
        print("*"+' '*(n-2)+"*")
