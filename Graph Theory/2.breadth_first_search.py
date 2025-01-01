'''
Breadth First Search for Graph Traversal
- Recursive
- Back Tracking Approach
'''

from collections import deque

def BFS(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    
    while queue:
        vertex = queue.popleft()
        print(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D':['B'],
    'E': ['B'],
    'F':['C'],
    'G':['C']
}

BFS(graph, 'A')