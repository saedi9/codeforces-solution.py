t = int(input())
while t:
  t-=1
  s = input()
  a,b = 0,0
  for i in range(0,len(s)):
    if s[i]=='A' or s[i]=='C':
      a+=1
    else:
      b+=1
  if a==b:
    print('YES')
  else:
    print('NO')