def isBad(a):
  if a % 3 == 0 or f'{a}'[len(f'{a}') - 1] == '3':
    return True
  return False


t = int(input())
for x in range(t):
  k = int(input())
  n = 0
  for i in range(k):
    n += 1
    while isBad(n):
      n += 1
  print(n)
