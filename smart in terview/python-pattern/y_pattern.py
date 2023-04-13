n=int(input())
for i in range(-n,n+1):
    a=""
    for j in range(1,2*n):
        if j==n+i and i<1:
            a=a+"*"
        elif j==n-i :
            a=a+"*"
        else:
            a=a+" "
    print(a)