t = int(input())
while t:
    t -= 1
    a = int(input())
    b = [int(x) for x in input().split()]
    c = set(b)
    if len(b) == len(c):
        print('YES')
    else:
        print('NO')
