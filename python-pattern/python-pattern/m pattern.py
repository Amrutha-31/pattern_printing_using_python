n=int(input())
c=0
a=(2*n)-1
for i in range(n):
    if i==0:
        hallow="  "*((2*n)-2)
        print("* "+hallow+"* ")
    elif i>=1 and i<=n-1:
        right = '  ' * (i-1)
        left="  "*(c)
        hallow="  "*((a-i)-i-1)
        print("* "+left+"* "+hallow+"* "+right+"* ")
        c=c+1