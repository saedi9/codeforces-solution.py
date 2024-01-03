n = int(input())
p = [int(x) for x in input().split()]
res = 0.0

for i in range(n):
  res += (p[i] / n)

print("%.12f" % res)
