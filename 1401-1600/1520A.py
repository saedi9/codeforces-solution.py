def polyCarp(s):
  a = set(s[0])
  for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
      if s[i + 1] in a:
        return False
      a.add(s[i + 1])
  return True


t = int(input())

for i in range(t):
  n = input()
  s = input()
  if polyCarp(s):
    print('YES')
  else:
    print('NO')

# def polyCarp(s):
#   a = [0] * 256
#   a[ord(s[0])] =1
#   for i in range(len(s) - 1):
#     if s[i] != s[i + 1]:
#       if a[ord(s[i + 1])] == 1:
#         return False
#       a[ord(s[i+1])] =1
#   return True
#
#
# t = int(input())
#
# for i in range(t):
#   n = input()
#   s = input()
#   if polyCarp(s):
#     print('YES')
#   else:
#     print('NO')
