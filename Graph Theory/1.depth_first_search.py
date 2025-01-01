'''
DFS for Graph Traversal
- Recursive Approach
- Backtracking
'''
def DFS(graph, start_node, visited = None):
    if visited is None:
        visited = set()
        
    visited.add(start_node)
    print(start_node)
    
    for nodes in graph[start_node]:
        if nodes not in visited:
            DFS(graph, nodes, visited)
    

graph_two = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D':['B'],
    'E': ['B'],
    'F':['C'],
    'G':['C']
}
DFS(graph_two, 'A')