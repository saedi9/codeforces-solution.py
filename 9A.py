w, y = [int(x) for x in input().split()]
d = 6 - max(w, y) + 1
p = ['0/1','1/6','1/3','1/2','2/3','5/6','1/1']
print(p[d])

