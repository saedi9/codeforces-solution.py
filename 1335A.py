t = int(input())

for x in range(t):
  n = int(input())
  if n > 2:
    print(int(n / 2) if n % 2 != 0 else int(n / 2) - 1)
  else:
    print(0)
