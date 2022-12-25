k, n, w = [int(x) for x in input().split()]
res = int((((w * (w + 1)) / 2) * k - n))
if res <= 0:
  print('0')
else:
  print(res)
