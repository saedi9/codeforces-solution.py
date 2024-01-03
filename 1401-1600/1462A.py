import collections
t = int(input())
while t:
  t -= 1
  n = int(input())
  l = [int(x) for x in input().split()]
  q = collections.deque(l)
  l = []
  while q:
    l.append(q.popleft())
    if q:
      l.append(q.pop())
  print(*l,sep=' ')