t = int(input())
while t:
    t -= 1
    a, b, c = [int(x) for x in input().split()]
    if a + b >= 10 or a+c >= 10 or b+c >= 10:
        print("YES")
    else:
        print("NO")
