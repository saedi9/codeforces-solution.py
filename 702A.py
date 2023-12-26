
l = int(input())
arr = [int(x) for x in input().split()]
mx, i = 1, 0

while i < l:
  c = 1
  while i < l-1 and arr[i] < arr[i+1]:
    i += 1
    c += 1
  i+=1
  if c>mx:
    mx = c

print(mx)