import math


def com(n):
  if n < 4:
    return False
  for i in range(2, int(n / 2) + 1):
    if n % i == 0:
      return True
  return False


n = int(input())
f, s = math.ceil(n / 2), math.floor(n / 2)
while s > 3:
  if com(f) and com(s):
    break
  f += 1
  s -= 1
print(f'{f} {s}')
