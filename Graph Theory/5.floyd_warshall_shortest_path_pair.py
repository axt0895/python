def floyd_warshall(graph):
    dist = [row[:] for row in graph]
    n = len(dist)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return dist


graph = [
    [0, 2, float('inf'), 1, float('inf')],
    [float('inf'), 0, 3, float('inf'), float('inf')],
    [float('inf'), float('inf'), 0, 4, 2],
    [float('inf'), float('inf'), float('inf'), 0, 5],
    [float('inf'), float('inf'), float('inf'), float('inf'), 0]
]

results = floyd_warshall(graph)

for row in results:
    print(row)