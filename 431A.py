a = [int(x) for x in input().split()]
s = input()
res=0
for i in s:
  res+=a[int(i)-1]
print(res)