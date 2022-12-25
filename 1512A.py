# t = int(input())

# while t:
#   t-=1
#   n = int(input());
#   a = input().split()
#   for i in a:
#     if a.count(i)==1:
#       print(a.index(i)+1)
#       break


t = int(input())

while t:
  t -= 1
  n = int(input())
  a = input().split()
  print(a.index(min(a, key=a.count)) + 1)
