a, b = [int(x) for x in input().split()]
print(f'{min(a, b)} {int((max(a, b) - min(a, b)) / 2)}')
