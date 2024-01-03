t = int(input())
while t:
  t -= 1
  n = int(input())
  a = [int(x) for x in input().split()]
  b = [int(x) for x in input().split()]
  ma = min(a)
  mb = min(b)
  res = 0
  for i in range(n):
    res += max(a[i] - ma, b[i] - mb)
  print(res)
