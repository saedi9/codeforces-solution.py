t = int(input())
while t:
  t -= 1
  n, m = [int(x) for x in input().split()]
  if n == 1:
    print(0)
  elif n == 2:
    print(m)
  else:
    print(2 * m)
