N=int(input())
M=int(input())
for i in range(1,N+1):
        if i%2!=0 and i<(N):
            c=M-(3*i)
            a="-"*((c//2))
            b=".|."*i
            print(a+b+a)
        elif i==N:
            a="-"*(N)
            b="WELCOME"
            print(a+b+a)
N=int(input())
M=int(input())
for i in range(1,N+1):
   if i%2!=0 and i<=N+1:
        N=N-2
        d=M-(3*N)
        e="-"*((d//2))
        f=".|."*(N)
        print(e+f+e)
d=M-(3*1)
e="-"*((d//2))
f=".|."*(1)
print(e+f+e)