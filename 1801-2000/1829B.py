t = int(input())
while t:
  t -= 1
  n = int(input())
  a = input().split()
  i, ans = 0, 0
  while i < n:
    tem = 0
    while i < n and a[i] == '0':
      i += 1
      tem += 1
    i += 1
    ans = max(tem, ans)
  print(ans)
