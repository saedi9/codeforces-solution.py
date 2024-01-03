n = int(input())

tot = 1
i = 1
while n >= (tot+ int(((i+1)*(i+2))/2)):
  i += 1
  tot += int((i*(i+1))/2)
print(i)
