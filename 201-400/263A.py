a = []
for i in range(5):
  a.append(input().split())

ind = [0, 0]
for i in range(len(a)):
  for j in range(len(a[i])):
    if a[i][j] == '1':
      ind = [i, j]
      break
print(abs(ind[0] - 2) + abs(ind[1] - 2))
