t = int(input())
while t:
  t -= 1
  n = int(input())
  c = [int(x) for x in input().split()]
  mn = min(c)
  res=0
  for i in c:
    res+=i-mn
  print(res)