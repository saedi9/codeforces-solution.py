s = input()
l = 0
for c in s:
  if c == '4' or c == '7':
    l += 1

if l == 4 or l == 7:
  print('YES')
else:
  print('NO')
