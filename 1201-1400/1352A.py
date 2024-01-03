import math

t = int(input())

for o in range(t):
  n = input()
  ln = ''
  l = 0
  for i in range(len(n) - 1):
    if n[i] != '0':
      ln += f'{int(int(n[i]) * math.pow(10, len(n) - i - 1))} '
      l += 1
  if n[-1] != '0':
    ln += n[-1]
    l += 1
  print(l)
  print(ln)
