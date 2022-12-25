t = int(input())
for i in range(t):
  input()
  a = [int(x) for x in input().split()]
  mx, mn = -1, 1000000000
  for x in a:
    if x < mn: mn = x
    if x > mx: mx = x

  print(mx - mn)

# t= int(input())
# for i in range(t):
#   input()
#   a = [int(x) for x in input().split()]
#   print(max(a)-min(a))
