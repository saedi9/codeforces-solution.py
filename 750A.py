import math

n, k = [int(x) for x in input().split()]

if 5 * ((n * (n + 1)) / 2) <= 240 - k:
  print(n)
else:
  print(int((math.sqrt(int((240 - k) / 5) * 2 * 4 + 1) - 1) / 2))
