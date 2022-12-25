n, k = [int(x) for x in input().split()]
num = [int(x) for x in input().split()]
res = 0
for i in range(len(num)):
  if num[i] != 0 and num[i] >= num[k - 1]:
    res += 1
print(res)
