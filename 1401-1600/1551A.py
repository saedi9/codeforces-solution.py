t = int(input())
while t:
  t -= 1
  n = int(input())
  print(f'{n - round(n / 3) * 2} {round(n / 3)}')
