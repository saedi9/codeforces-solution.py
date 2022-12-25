t = int(input())
number = 1
while t:
  print(f't: {number}')
  t -= 1
  number += 1
  n, k = [int(x) for x in input().split()]
  a = [int(x) for x in input().split()]
  b = [int(x) for x in input().split()]
  print(f'a: {a} b: {b} k: {k}')
  a.sort()
  b.sort()
  # n -= 1
  # k -= 1
  ap = k - 1
  bp = n - 1
  while k > 0 and ap >= 0:
    if b[bp] > a[ap] and ap >= 0:
      a[ap] = b[bp]
      k -= 1
      bp -= 1
    ap -= 1

  # while b[n] > a[k] and k >= 0:
  #   print(a[k], b[n])
  #   a[k] = b[n]
  #   n -= 1
  #   k -= 1
  # 3 2 --- 2 3
  # 1 4 --- 1 4

  print(sum(a))
