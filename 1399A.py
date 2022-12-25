t = int(input())

for x in range(t):
  n = int(input())
  l = [int(x) for x in input().split()]
  l.sort()
  isP = True
  for i in range(1, len(l)):
    if l[i] - l[i - 1] > 1:
      isP = False
      break
  if isP:
    print("YES")
  else:
    print("NO")
