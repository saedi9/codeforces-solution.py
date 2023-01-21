t = int(input())
while t:
  t-=1
  a, b, c, d = [int(x) for x in input().split()]
  if max(a, b) >= min(c, d) and max(c,d)>=min(a,b):
    print('YES')
  else:
    print('NO')
