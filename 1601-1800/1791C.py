t = int(input())

while t:
    t -= 1
    n = int(input())
    s = input()
    ans = 0
    for i in range(n//2):
        if s[i] == s[n-i-1]:
            ans = n - 2*i
            break
    if ans == 0 and n % 2 != 0:
        print(ans+1)
    else:
        print(ans)
