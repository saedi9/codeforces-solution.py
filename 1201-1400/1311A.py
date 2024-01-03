t = int(input())
while t:
  t -= 1
  a, b = [int(x) for x in input().split()]
  if a < b:
    if (b - a) % 2 == 0:
      print(2)
    else:
      print(1)
  elif a > b:
    if (a - b) % 2 == 0:
      print(1)
    else:
      print(2)
  else:
    print(0)
