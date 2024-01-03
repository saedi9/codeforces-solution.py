n = int(input())
s = 0
for i in range(n):
  a = [int(x) for x in input().split(' ')]
  res = 0
  for x in range(len(a)):
    res += a[x]
  if res > 1:
    s += 1
print(s)
