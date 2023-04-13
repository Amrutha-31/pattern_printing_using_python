n=int(input())
a=65
c=n-1
for i in range(1,2*n):
    if i==1:
        print(" "*(n-1)+chr(a))
        a=a+1
    elif i<=n:
        spaces=" "*(n-i)
        hallow="  "*(i-2)
        print(spaces+chr(a)+" "+hallow+chr(a))
        a=a+1
    elif i<(2*n)-1 and i!=n:
        spaces=" "*(i-n)
        hallow="  "*(c-2)
        print(spaces+chr(a-2)+" "+hallow+chr(a-2))
        c=c-1
        a=a-1
    else:
        a=a-2
        print(" "*(n-1)+chr(a))