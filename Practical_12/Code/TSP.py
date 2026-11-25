def tsp():
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    n = len(graph)
    visited = [False] * n
    visited[0] = True
    def travel(city, count, cost):
        if count == n:
            return cost + graph[city][0]
        ans = float('inf')
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                ans = min(ans, travel(i, count + 1,
                                      cost + graph[city][i]))
                visited[i] = False
        return ans
    print("Minimum travelling cost:", travel(0, 1, 0))

tsp()