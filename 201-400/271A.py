y = int(input())

while y <= 9999:
  y += 1
  if len(set(f'{y}')) == 4:
    break
print(y)
