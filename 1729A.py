t = int(input())
while t:
    t -= 1
    a, b, c = [int(x) for x in input().split()]
    # print('a',abs(a - 1))
    # print('b',abs(abs(c-b)+abs(c-1)))
    if abs(a - 1) < abs(abs(c-b)+abs(c-1)):
        print(1)
    elif abs(abs(c-b)+abs(c-1)) < abs(a-1):
        print(2)
    else:
        print(3)
