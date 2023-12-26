t = int(input())
while t:
  t-=1
  n = int(input())
  a = [int(x) for x in input().split()]
  evr = odr = 0
  for i in a:
    if i%2==0:
      evr+=i
    else:
      odr+=i
  if evr>odr:
    print("YES")
  else:
    print('NO')