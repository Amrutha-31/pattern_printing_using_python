n=int(input())
a=0
for i in range(1,n+1):
    if i==1:
        print(' '*(n-1)+"*")
    elif i>=2 and i!=(n//2):
        print(' '*(n-i)+"*"+' '*(i+a)+"*")
        i=i+1
        a=a+1
    elif i==(n//2):
        print(' '*(n//2)+"*"*(n))