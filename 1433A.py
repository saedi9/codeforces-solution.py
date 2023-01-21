def getD(d, td):
  if int(d/1000) == 9:
    return 1
  if len(f'{d}') >= 4:
    return int(d / 1000) + 1
  return int(f'{d}'[0] * td)


t = int(input())
while t:
  t -= 1
  x = input()
  d, td, res, dp = 1, 1, 0, 1
  ba = f'{d}'
  while f'{d}' <= x:
    res += len(f'{d}')
    td = td % 4 + 1
    d = getD(d, td)
    if d >= 9999:
      break
  if d == int(x):
    res+=4
  print(res)
