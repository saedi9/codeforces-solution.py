t = int(input())
while t:
    t -= 1
    c = 0
    s = input()
    for i in range(0, 10):
        if s[i] != 'codeforces'[i]:
            c += 1
    print(c)
