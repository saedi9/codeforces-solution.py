f = input()
s = input()
res = ''

for i in range(len(f)):
  if f[i] == s[i]:
    res += '0'
  else:
    res += '1'

print(res)
