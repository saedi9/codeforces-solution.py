d = [int(x) for x in input().split()]
d.sort()

b = d[0] + d[2] - d[3]

a = d[0] - b
c = d[2] - b

print(a, b, c)
