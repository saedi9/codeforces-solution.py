n = input()
num = [int(x) for x in input().split()]

mn, mx, res = num[0], num[0], 0

for i in num:
  if i > mx:
    res += 1
    mx = i
  if i < mn:
    res += 1
    mn = i

print(res)
