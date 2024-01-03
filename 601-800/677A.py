n, h = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
res = 0

for i in a:
  if i > h:
    res += 2
  else:
    res += 1

print(res)
