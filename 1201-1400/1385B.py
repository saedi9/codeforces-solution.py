t = int(input())

while t:
  t -= 1
  n = int(input())
  a=input().split()
  res = []
  for i in a:
    if i not in res:
      res.append(i)
  print(' '.join(res))