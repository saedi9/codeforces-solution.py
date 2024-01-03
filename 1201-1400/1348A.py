t = int(input())

while t:
  t -= 1
  n = int(input())
  res = 0
  for i in range(1, int(n / 2) + 1):
    res += 2 ** i
  print(res)
