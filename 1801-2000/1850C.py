t = int(input())

while t:
  t-=1
  res=''
  for i in range(8):
    s = input()
    for j in s:
      if j != '.':
        res+=j
  print(res)