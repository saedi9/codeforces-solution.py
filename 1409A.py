import math

t = int(input())

for i in range(t):
  a, b = [int(x) for x in input().split()]
  a, b = max(a, b), min(a, b)
  r = a - b
  if r == 0:
    print(0)
  elif r > 10:
    print(int(math.ceil(r / 10)))
  elif r <= 10:
    print(1)
