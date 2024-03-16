t = int(input())

while t:
  t-=1
  a,b,n = [int(x) for x in input().split()]
  a,b = max(a,b),min(a,b)
  ans = 0
  while a<=n:
    b+=a
    a,b=b,a
    ans+=1
  print(ans)