k, r = [int(x) for x in input().split()]
res = 1
while True:
  if (k * res - r) % 10 == 0:
    break
  elif k * res % 10 == 0:
    break
  res += 1
print(res)
