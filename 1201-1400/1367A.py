t = int(input())

for x in range(t):
  b = input()
  res = f'{b[:2]}'
  for i in range(3, len(b), 2):
    res += b[i]

  print(res)
