'''
- Topological Sort
- maintain the order of grap
- linear order, such that A comes before B in graph
- very useful in many real world scenarios
'''

def topological_sort_dfs(graph):
    stack = []
    visited = set()
    
    def DFS(node):
        visited.add(node)
        for neighnor in graph[node]:
            if neighnor not in visited:
                DFS(neighnor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            DFS(node)
            
    return stack[::-1]

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

print(topological_sort_dfs(graph))

'''
graph_ = {
    'A': ['B', 'C', 'E'],
    'B': ['D', 'F'],
    'C': ['D', 'G'],
    'D': ['H', 'I'],
    'E': ['F', 'G'],
    'F': ['J'],
    'G': ['J'],
    'H': ['K'],
    'I': ['K'],
    'J': ['L', 'M'],
    'K': ['N'],
    'L': ['N'],
    'M': ['N'],
    'N': []
}'''