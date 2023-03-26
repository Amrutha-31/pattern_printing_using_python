n=int(input())
for i in range(1,n+1):
    if i==1:
        print("* "*((2*n)-1))
    else:
        spaces_l=" "*(i-1)
        spaces_r=" "*(i+1)
        hallow="  "*(i-2)
        print(spaces_l+"* "*(n-i+1)+hallow+"* "*(n-i+1)+spaces_r)