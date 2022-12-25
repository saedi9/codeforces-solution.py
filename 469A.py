n = int(input())

p = input().split()
q = input().split()

s = set(p[1:])
s.update(q[1:])

if len(s) == n:
  print('I become the guy.')
else:
  print('Oh, my keyboard!')
