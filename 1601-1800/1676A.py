t = int(input())
while t:
  t -= 1
  s = list(input())
  s1, s2 = 0, 0
  for i in range(int(len(s) / 2)):
    s1 += int(s[i])
  for i in range(3, len(s)):
    s2 += int(s[i])
  if s1 == s2:
    print('YES')
  else:
    print('NO')
