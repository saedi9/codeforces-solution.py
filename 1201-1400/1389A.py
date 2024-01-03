t = int(input())
while t:
  t-=1
  l,r = [int(x) for x in input().split()]
  x = l
  y = x*2
  if y<=r:
    print(x,y)
  else:
    print(-1,-1)