n = int(input())
res = 0

for i in range(n):
  p, q = [int(x) for x in input().split()]
  if q - p >= 2:
    res += 1

print(res)
