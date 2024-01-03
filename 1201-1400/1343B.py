def l(n):
  t = int(n / 2)
  for i in range(t):
    print(2 * i + 2, end=' ')
  for i in range(t - 1):
    print(2 * i + 1, end=' ')
  print(t * (t + 1) - (t - 1) * (t - 1))


t = int(input())

for x in range(t):
  n = int(input())
  if (n / 2) % 2 != 0:
    print('NO')
  else:
    print('YES')
    l(n)
