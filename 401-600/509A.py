n = int(input())

pr = [1]*n
cr = [1]*n

for i in range(1, n):
    for j in range(1, n):
        cr[j] = pr[j]+cr[j-1]
    pr = cr

print(cr[n-1])
