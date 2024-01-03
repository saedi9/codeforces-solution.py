t = int(input())

while t:
  t-=1
  n = int(input())
  s = [int(x) for x in input().split()]
  on = 0
  for x in s:
    if x%2!=0:
      on+=1
  if on == n:
    print('Yes')
  else:
    print('No')