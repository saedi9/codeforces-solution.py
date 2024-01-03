import math


def isPrime(n):
  if 4 > n > 1:
    return True
  for i in range(2,int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False

  return True


def nextPrime(n):
  x = n + 1
  while not isPrime(x):
    x += 1
  return x


n, m = [int(x) for x in input().split()]
h = nextPrime(n)
if h == m:
  print('YES')
else:
  print('NO')