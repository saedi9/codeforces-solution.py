n = int(input())
mr, cr = 0, 0
for i in range(n):
  m, c = [int(x) for x in input().split()]
  if c > m:
    cr += 1
  elif c < m:
    mr += 1

if mr > cr:
  print('Mishka')
elif mr < cr:
  print('Chris')
else:
  print('Friendship is magic!^^')
