# Implement prim’s algorithm #
n = int(input("Enter number of vertices: "))

graph = []
print("Enter adjacency matrix:")

for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [False] * n
visited[0] = True

total = 0
count = 0

print("\nEdges of Minimum Spanning Tree:")

while count < n - 1:
    minimum = float('inf')
    x = -1
    y = -1

    for i in range(n):
        if visited[i]:
            for j in range(n):
                if not visited[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    if x == -1:
        print("Graph is disconnected.")
        break

    print(x + 1, "-", y + 1, "Weight:", minimum)

    visited[y] = True
    total += minimum
    count += 1

if count == n - 1:
    print("Minimum cost:", total)