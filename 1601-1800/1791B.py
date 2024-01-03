t = int(input())
while t:
    t -= 1
    l = int(input())
    s = input()
    p = False
    loc = [0, 0]
    for i in range(0, l):
        if s[i] == "R":
            loc[0] = loc[0]+1
        elif s[i] == "L":
            loc[0] = loc[0]-1
        elif s[i] == "U":
            loc[1] = loc[1]+1
        elif s[i] == "D":
            loc[1] = loc[1]-1
        if not p:
            if loc[0] == 1 and loc[1] == 1:
                p = True
    if p:
        print('YES')
    else:
        print('NO')
