t =  int(input())
while t:
  t-=1
  a,b,c,n = [int(x) for x in  input().split()]
  mx = max([a,b,c])
  n -= (mx -a)
  n -= (mx -b)
  n -= (mx -c)
  if n>=0 and n%3==0:
    print('YES')
  else:
    print('NO')