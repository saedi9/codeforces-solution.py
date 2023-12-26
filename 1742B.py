t = int(input())
while t:
    t -= 1
    a = int(input())
    b = set([int(x) for x in input().split()])
    if len(b) == a:
        print('YES')
    else:
        print('NO')
