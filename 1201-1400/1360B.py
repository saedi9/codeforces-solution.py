t = int(input())
while t:
  t -= 1
  n = int(input())
  a = [int(x) for x in input().split()]
  a.sort()
  mn = 100000
  for i in range(1, len(a)):
    mn = min(mn, a[i] - a[i - 1])

  print(mn)
