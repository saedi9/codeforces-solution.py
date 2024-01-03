t = int(input())
while t:
  t-=1
  n=int(input())
  win = -1
  qm = -1
  for i in range(n):
    a,b=[int(x) for x in input().split()]
    if a <= 10:
      if qm<b:
        win = i+1
        qm = b
  print(win)