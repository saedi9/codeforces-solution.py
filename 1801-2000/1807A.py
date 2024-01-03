t = int(input())
while t:
    t -= 1
    a, b, c = [int(x) for x in input().split()]
    if a+b==c:
      print("+")
    else:
      print("-")
      