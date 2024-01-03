t = int(input())
while t:
  t-=1
  h,m=[int(x) for x in input().split()]
  if h == 0:
    print(24*60-m)
  else:
    print((24-h)*60-m)