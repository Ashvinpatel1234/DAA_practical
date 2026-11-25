def dfs(graph, start, visited):
    if start not in visited:
        visited.add(start)
        print(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': [],
}
visited = set()
dfs(graph, 'A', visited)