n = input()
a = [int(x) for x in input().split()]

mx = max(a)
res = 0

for i in a:
  res += (mx - i)
print(res)
