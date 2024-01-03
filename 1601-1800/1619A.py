t = int(input())
while t:
  t -= 1
  a = input()
  if len(a) % 2 != 0:
    print("NO")
  else:
    if a[0:int(len(a) / 2)] == a[int(len(a) / 2):len(a)]:
      print("YES")
    else:
      print("NO")
