t = int(input())
while t:
  t -= 1
  n = int(input())
  a = [int(x) for x in input().split()]
  s1, s2 = 0, 0
  for i in a:
    if i == 1:
      s1 += 1
    else:
      s2 += 1
  if s2 % 2 != 0 and s1 > 0 and (s1 - 2) % 2 == 0:
    print("YES")
  elif s1 % 2 == 0 and s2 % 2 == 0:
    print('YES')
  else:
    print('NO')
