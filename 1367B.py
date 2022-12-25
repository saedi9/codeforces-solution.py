def isOdd(n):
  if n % 2 == 0:
    return False
  return True


t = int(input())
while t > 0:
  t -= 1
  n = input()
  a = [int(x) for x in input().split()]
  od, ev = 0, 0
  for i, d in enumerate(a):
    if isOdd(d):
      if not isOdd(i):
        od += 1
    else:
      if isOdd(i):
        ev += 1
  if ev == od and ev == 0:
    print(0)
  elif ev == od:
    print(od)
  else:
    print(-1)
  # print(f'ev: {ev} od: {od}')
