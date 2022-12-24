t = int(input())
while t > 0:
  t -= 1
  x, y, n = [int(x) for x in input().split()]
  mx = 0
  for i in range(n, 1, -1):
    if x >= n:
      break
    if i % x == y:
      mx = max(i, mx)
      break

  print(mx)
