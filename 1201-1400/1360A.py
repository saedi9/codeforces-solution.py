t = int(input())
while t:
  t -= 1
  a, b = [int(x) for x in input().split()]
  a, b = max(a, b), min(a, b)
  b *= 2
  a = max(a, b)
  print(a * a)
