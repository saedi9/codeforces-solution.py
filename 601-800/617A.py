n = int(input())
res, s = 0, 5
while n > 0:
  res += int(n / s)
  n %= s
  s -= 1
print(res)
