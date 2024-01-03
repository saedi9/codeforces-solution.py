n = input()
l = input()
s = set()
for i in l:
  s.update(i.lower())

if len(s) == 26:
  print('YES')
else:
  print('NO')
