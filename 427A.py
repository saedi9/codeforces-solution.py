n = input()
l = [int(x) for x in input().split()]
p, res = 0, 0

for i in l:
  if i == -1:
    if p > 0:
      p += i
    else:
      res += 1
  else:
    p += i
print(res)
