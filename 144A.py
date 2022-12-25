n = int(input())
a = [int(x) for x in input().split()]

m, mi, mx, mxi = 9999, 0, -1, 0

for i in range(n):
  if a[i] <= m:
    mi = i
    m = a[i]
  if a[i] > mx:
    mx = a[i]
    mxi = i

if mi < mxi:
  print(n - mi - 1 + mxi - 1)
else:
  print(n - mi - 1 + mxi)
