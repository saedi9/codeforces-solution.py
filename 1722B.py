t = int(input())
h = 'BG'
while t:
  t -= 1
  col = int(input())
  r1 = input()
  r2 = input()
  f = True
  for i in range(0, col):
    if r1[i] != r2[i]:
      print(r1[i],r2[i])
      if r1[i] not in h or r1[i] in h and r2[i] not in h:
        f = False
        break
  if f:
    print('YES')
  else:
    print('NO')
