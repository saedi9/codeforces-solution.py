n = int(input())
a = int(n/2)
p = []
if n - a*2==1:
  a-=1
for i in range(a):
  p.append(2)
if n != a*2:
  p.append(3)
print(len(p))
print(*p)
