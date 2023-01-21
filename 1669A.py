t = int(input())
while t:
  t -= 1
  n = int(input())
  if n <= 1399:
    print('Division 4')
  elif 1400 <= n <= 1599:
    print('Division 3')
  elif 1600 <= n <= 1899:
    print('Division 2')
  elif 1900 <= n:
    print('Division 1')
