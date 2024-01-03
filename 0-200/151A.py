n, k, l, c, d, p, nl, np = [int(x) for x in input().split()]

print(int(min(int((k * l) / nl), c * d, int(p / np)) / n))
