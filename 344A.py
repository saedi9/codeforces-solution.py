n = int(input())
pr = ''
res = 0
for i in range(n):
  t = input()
  if pr != t:
    res += 1
    pr = t

print(res)
