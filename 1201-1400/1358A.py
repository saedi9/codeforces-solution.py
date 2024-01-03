import math

t = int(input())

while t:
  t-=1
  a,b = [int(x) for x in input().split()]
  print(math.ceil((a*b)/2))