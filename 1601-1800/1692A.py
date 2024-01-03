t = int(input())
while t:
  t -= 1
  l = [int(x) for x in input().split()]
  res = 0
  for i in range(1, len(l)):
    if l[0] < l[i]:
      res += 1

  print(res)
