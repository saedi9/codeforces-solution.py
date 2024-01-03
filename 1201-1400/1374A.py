t = int(input())
while t > 0:
  t -= 1
  x, y, n = [int(x) for x in input().split()]
  mx = 0
  if (int(n / x) * x + y) > n:
    print((int(n / x) - 1) * x + y)
  else:
    print(int(n / x) * x + y)
