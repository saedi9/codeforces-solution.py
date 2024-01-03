def getIdx(h, i, j):
  for x in j:
    if i == h[x]:
      j.remove(x)
      return x + 1
  return -1


n = int(input())
a = input().split()
idx = []
idT = [i for i in range(n)]
sk = '123'

while True:
  lin = []
  for i in sk:
    tem = getIdx(a, i, idT)
    if tem == -1:
      break
    else:
      lin.append(tem)
  if len(lin) < 3:
    break
  idx.append(lin)

print(len(idx))
for i in idx:
  print(*i)
