n = int(input())

h, a = [], []

for i in range(n):
  b, c = [x for x in input().split()]
  h.append(b)
  a.append(c)

res = 0

for i in h:
  for j in a:
    if i == j:
      res += 1

print(res)
