t = int(input())
while t:
  t-=1
  n = int(input())
  a = [int(x) for x in input().split()]
  d = {}
  ans = -1
  for i in a:
    if i in d:
      d[i]+=1
    else:
      d[i]=1
    if d[i]>=3:
      ans = i
      break
  print(ans)