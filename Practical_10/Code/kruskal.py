def find(parent, v):
    while parent[v] != v:
        v = parent[v]
    return v

n = int(input("Enter number of vertices: "))

graph = []
print("Enter adjacency matrix (0 for no edge):")

for i in range(n):
    graph.append(list(map(int, input().split())))

edges = []

for i in range(n):
    for j in range(i + 1, n):
        if graph[i][j] != 0:
            edges.append((graph[i][j], i, j))

edges.sort()

parent = list(range(n))
total = 0
count = 0

print("\nEdges of Minimum Spanning Tree:")

for weight, u, v in edges:
    p1 = find(parent, u)
    p2 = find(parent, v)

    if p1 != p2:
        print(u + 1, "-", v + 1, "Weight:", weight)
        parent[p1] = p2
        total += weight
        count += 1

    if count == n - 1:
        break

if count == n - 1:
    print("Minimum cost:", total)
else:
    print("Graph is disconnected.")