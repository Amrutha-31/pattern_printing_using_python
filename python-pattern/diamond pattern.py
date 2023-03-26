n = int(input())
k = n-1
for i in range(1,n+1):
  space = " " * k
  stars = "* " * i
  print(space + stars)
  k =k-1
 
k = n
for i in range(1, n):
    spaces =" " * i
    stars = "* " * (k-i)
    print(spaces + stars)