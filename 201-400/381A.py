from collections import deque

n = int(input())
q = deque([int(x) for x in input().split()])
s, d = 0, 0
isS = True

while len(q) > 0:
  if q[0] > q[-1]:
    if isS:
      s += q.popleft()
      isS = False
    else:
      d += q.popleft()
      isS = True
  else:
    if isS:
      s += q.pop()
      isS = False
    else:
      d += q.pop()
      isS = True

print(s, d)

# print(len(q))

# q.pop()
# print(q)
# print(len(q))
