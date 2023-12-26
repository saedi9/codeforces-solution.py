t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = [int(x) for x in input().split()]
    n = sum(arr)
    if n % 2 == 0:
        print("YES")
    else:
        print("NO")
