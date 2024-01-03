n = int(input())
mx = -1
c = 0
for i in range(n):
  a, b = [int(x) for x in input().split()]
  c = (c - a) + b
  if c > mx:
    mx = c
print(mx)
