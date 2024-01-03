t = int(input())
while t:
  t -= 1
  n = input()
  res = (len(n) - 1) * 9
  mx = int(n[0] * len(n))
  if int(n) < mx:
    res += (int(n[0]) - 1)
  else:
    res += int(n[0])
  print(res)
