t = int(input())
while t:
  t -= 1
  n = int(input())
  l = [int(x) for x in input().split()]
  on = 0
  for i in l:
    if i%2==1:
      on+=1
  if on%2==1 or 0<on < n:
    print('YES')
  else:
    print('NO')