t = input()
h = input().split()
c = False

for i in h:
  if i[0]==t[0] or i[1]==t[1]:
    c = True
    break

if c:
  print('YES')
else:
  print('NO')