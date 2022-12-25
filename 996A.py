n = int(input())
res = 0
b = [100, 20, 10, 5, 1]

for i in b:
  res += (int(n / i))
  n %= i

print(res)
