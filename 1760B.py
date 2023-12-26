t = int(input())
while t:
    t -= 1
    l = int(input())
    s = input()
    mx = 0
    for i in range(0, len(s)):
        if ord(s[i]) > mx:
            mx = ord(s[i])
    print(mx-ord('a')+1)
