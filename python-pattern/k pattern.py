n=int(input())
for i in range(1,n+1):
    if i==1:
        print("*"+' '*(n-1)+"*")
    elif i<(n//2):
        print("*"+' '*(n-i)+"*"+' '*(n-i))
    elif i==(n//2):
        print("* "*(n//2))
    elif i>(n//2):
        print("*"+' '*(1+i)+"*")
