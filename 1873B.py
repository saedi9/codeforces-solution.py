t = int(input())
while t:
  t-=1
  n = int(input())
  a = [int(x) for x in input().split()]
  a.sort()
  a[0]+=1
  ans = 1
  for i in a:
    ans*=i
  print(ans)