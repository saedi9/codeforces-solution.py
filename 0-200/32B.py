s = input()
i = 0

while i < len(s):
  if s[i] == '.':
    print('0', end='')
  elif s[i] == '-':
    if s[i + 1] == '.':
      print('1', end='')
    elif s[i + 1] == '-':
      print('2', end='')
    i += 1
  i += 1
print()
