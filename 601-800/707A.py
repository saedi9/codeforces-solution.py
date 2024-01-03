def isBlack(a):
  for i in a:
    if i in c:
      return False
  return True


n, m = [int(x) for x in input().split()]
isb = True
colors = []

for i in range(n):
  colors.append(input())
c = ['C', 'M', 'Y']

for i in colors:
  if not isBlack(i.split()):
    isb = False
    break

if isb:
  print('#Black&White')
else:
  print('#Color')
