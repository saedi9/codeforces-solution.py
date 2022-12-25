n = int(input())
x = 0
for i in range(n):
  s = input()
  if s[0] == 'X':
    if s[1] == '-':
      x -= 1
    else:
      x += 1
  elif s[0] == '+':
    x += 1
  else:
    x -= 1
print(x)
