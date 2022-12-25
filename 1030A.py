n = input()
s = input().split()

easy = True

for i in s:
  if i == '1':
    easy = False
    break

if easy:
  print("EASY")
else:
  print('HARD')
