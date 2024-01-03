from collections import Counter

h = input()
g = input()
p = input()

if Counter(list(h + g)) == Counter(list(p)):
  print('YES')
else:
  print('NO')
