n = int(input())
if n <= 1 or n%2!=0:
    print(-1)
else:
  f = True
  for i in range(1,n+1):
    if f:
      print(i+1,end=' ')
      f=False
    else:
      print(i-1,end=' ')
      f=True
