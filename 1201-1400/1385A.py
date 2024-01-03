t = int(input())
while t:
    t -= 1
    l = sorted([int(x) for x in input().split()])
    if l[2] == l[1]:
        print("YES")
        print(l[2], l[0], l[0])
    else:
        print("NO")
