edges = [
    (1, 'A', 'B'),
    (3, 'A', 'C'),
    (2, 'A', 'D'),
    (4, 'B', 'D'),
    (5, 'C', 'D')
]

edges.sort()

parent = {}

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x

for edge in edges:
    w, u, v = edge
    if u not in parent:
        parent[u] = u
    if v not in parent:
        parent[v] = v

mst = []
for w, u, v in edges:
    if find(u) != find(v):
        union(u,v)
        mst.append((u,v,w))