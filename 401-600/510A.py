n, m = [int(x) for x in input().split()]

r = False

for i in range(n):
  if i % 2 == 0:
    print('#' * m)
  else:
    if r:
      print(f'#{"." * (m - 1)}')
      r = False
    else:
      print(f'{"." * (m - 1)}#')
      r = True
