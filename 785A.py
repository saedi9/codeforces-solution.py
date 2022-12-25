s = {
  'Tetrahedron': 4,
  'Cube': 6,
  'Octahedron': 8,
  'Dodecahedron': 12,
  'Icosahedron': 20
}

n = int(input())
res = 0
for i in range(n):
  w = input()
  res += s[w]

print(res)
