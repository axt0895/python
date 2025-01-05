import heapq

def dijkstra(graph, start, end):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0

    previous_path = {node: None for node in graph}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node == end:
            break
        
        if current_distance > shortest_distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                previous_path[neighbor] = current_node
                
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Reconstruct path
    path = []
    current_node = end
    while current_node:
        path.append(current_node)
        current_node = previous_path[current_node]
    path.reverse()

    return shortest_distances[end], path

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

start = 'A'
end = 'F'
distance, path = dijkstra(graph, start, end)

print(f"Shortest distance from {start} to {end}: {distance}")
print(f"Shortest path: {' -> '.join(path)}")
