d = [int(x) for x in input().split()]
d.sort()
print(d[2] - d[1] + d[1] - d[0])
