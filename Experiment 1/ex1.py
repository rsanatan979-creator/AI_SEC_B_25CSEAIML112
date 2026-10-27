from collections import deque

def bfs_traversal(graph, start_node):
    visited = set()
    queue = deque()

    # Initialize setup
    visited.add(start_node)
    queue.append(start_node)

    print("BFS Traversal Order:", end=" ")

    while queue:
        current = queue.popleft()
        print(current, end=" ")

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}

start = 'A'
bfs_traversal(graph, start)