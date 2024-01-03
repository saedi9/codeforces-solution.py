n = int(input())
res = ''

for i in range(1, n):
  if i % 2 != 0:
    res += 'I hate that '
  else:
    res += 'I love that '

if n % 2 != 0:
  res += 'I hate it'
else:
  res += 'I love it'

print(res)
