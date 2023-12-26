t = int(input())
while t:
  t -= 1
  col = int(input())
  r1 = input()
  r2 = input()
  f = True
  for i in range(0, col):
    if r1[i]!=r2[i]:
      if r1[i]=='R' or r2[i]=='R':
        f = False
        break
  if f:
    print('YES')
  else:
    print('NO')
