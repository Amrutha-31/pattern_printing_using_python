n=int(input())
a=1
for i in range(1,n+1):
    for j in range(1,2*n):
        dots=". "*(n-i)
        zeros="0 "*(a)
    print(dots+zeros+dots)
    a=a+2
a=n-1
for i in range(1,n):
    for j in range(1,2*n):
        dots=". "*(i)
        zeros="0 "*(j-2*i)
    print(dots+zeros+dots)
    a=a-2