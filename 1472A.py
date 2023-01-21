def even(n):
  if n % 2 == 0:
    return True
  return False


t = int(input())
while t:
  t -= 1
  w, h, n = [int(x) for x in input().split()]
  i = 0
  while True:
    if even(w):
      w /= 2
    elif even(h):
      h /= 2
    else:
      break
    i += 1
  if 2 ** i >= n:
    print('YES')
  else:
    print('NO')
