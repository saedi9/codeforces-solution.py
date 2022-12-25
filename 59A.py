s = input()
isu = 0
for c in s:
  if c.isupper():
    isu += 1
if isu > len(s) - isu:
  print(s.upper())
else:
  print(s.lower())
