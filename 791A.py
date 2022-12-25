a, b = [int(x) for x in input().split()]
res = 0
while a <= b:
  res += 1
  a *= 3
  b *= 2
print(res)
