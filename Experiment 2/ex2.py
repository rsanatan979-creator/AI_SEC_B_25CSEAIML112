def dfs_traversal(graph, start_node, visited_node=None):
    if visited_node is None:
        visited_node = set()

    visited_node.add(start_node)
    print(start_node, end=" ")

    for neighbour in graph[start_node]:
        if neighbour not in visited_node:
            dfs_traversal(graph, neighbour, visited_node)


# Example
example_graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f', 'g'],
    'e': ['f'],
    'f': ['g'],
    'g': []
}

print("DFS Traversal Order:", end=" ")
dfs_traversal(example_graph, 'a')
print()