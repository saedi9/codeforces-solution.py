def cal(a, s):
  for i in range(s - 1, len(a), s):
    a[i] = 1


k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

a = [0] * d
cal(a, k)
cal(a, l)
cal(a, m)
cal(a, n)

print(sum(a))
