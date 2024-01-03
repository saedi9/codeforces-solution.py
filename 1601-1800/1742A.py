t = int(input())
while t:
  t -= 1
  a = [int(x) for x in input().split()]
  a.sort()
  if a[0]+a[1]==a[2]:
    print('YES')
  else:
    print('NO')