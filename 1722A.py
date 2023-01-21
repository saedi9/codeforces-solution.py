t = int(input())
timur = "Timru"
while t:
  t -= 1
  n = int(input())
  if ''.join(sorted(input())) == timur:
    print('Yes')
  else:
    print('No')
