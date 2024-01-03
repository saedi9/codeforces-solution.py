t = int(input())

while t > 0:
  t -= 1
  n = int(input())

  mx = 1

  for i in range(n, 1, -1):
    if i % 2 == 0:
      mx = max(mx, int(i / 2))
      break
  print(mx)
