t = int(input())
while t:
  t -= 1
  n, k = [int(x) for x in input().split()]
  a = [int(x) for x in input().split()]
  b = [int(x) for x in input().split()]

  if k == 0:
    print(sum(a))
  else:
    a.sort()
    b.sort()
    ap = k - 1
    bp = n - 1
    while k > 0 and ap >= 0:
      if b[bp] > a[ap] and ap >= 0:
        a[ap], b[bp] = b[bp], a[ap]
        k -= 1
        b.sort()
      ap -= 1
    print(sum(a))
