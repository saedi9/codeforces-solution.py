import math

n = int(input())
f = int(n / 2)
s = int(math.ceil(n / 2))

print(f * (f + 1) - (s * s))
