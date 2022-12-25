s = input()
t = input()

isT = True

if len(s) == len(t):
  for i in range(len(s)):
    if s[i] != t[len(s) - i - 1]:
      isT = False
      break
else:
  isT = False

if isT:
  print("YES")
else:
  print("NO")
