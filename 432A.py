n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
res = 0

for i in a:
  if 5 - i >= k:
    res += 1

print(int(res / 3))
