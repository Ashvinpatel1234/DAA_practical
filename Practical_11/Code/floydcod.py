def floyd_warshall():
    d = [
        [0, 4, 999],
        [2, 0, 5],
        [999, 1, 0]
    ]

    n = len(d)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    print("Shortest Distance Matrix:")
    for row in d:
        print(row)

floyd_warshall()