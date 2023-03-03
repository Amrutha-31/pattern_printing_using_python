n=int(input())
for i in range(1,n+1):
    if i!=(n//2):
        print("*"+' '*(n-2)+"*")
    else:
        print("*"*n)
