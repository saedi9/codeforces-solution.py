s = input()
res = 0
sp = 'a'

for x in s:
  h = abs(ord(x) - ord(sp))
  if h <= 13:
    res += h
  else:
    res += (26 - h)
  sp = x

# for x in range(len(s)):
#   h = 0
#   if s[x]>sp:
#     h += ord(sp) - ord('a') + 1
#     h += ord('z') - ord(s[x])
#   else:
#     h += ord(s[x]) - ord('a') + 1
#     h += ord('z') - ord(sp)
#
#   res += min(h,abs(ord(s[x])-ord(sp)))
#   sp = s[x]
print(res)

# for x in range(ord('a'), ord('z')+1):
#   print(x - ord('a'),end=' ')
