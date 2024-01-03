n = int(input())
p = [int(x) for x in input().split()]
res = [0] * n

for i in range(n):
  res[p[i] - 1] = i + 1

for i in res:
  print(i, end=' ')
