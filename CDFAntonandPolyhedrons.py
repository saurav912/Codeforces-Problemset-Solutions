x = {'Tetrahedron':4,'Cube':6,'Octahedron':8,'Dodecahedron':12,'Icosahedron':20}
a = int(input())
p = 0
for i in range(a):
    p += x[input()]
print(p)
