graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 2,
    'G': 0
}


def astar(start, goal):
    open_list = [(start, 0)]
    came_from = {}
    g_cost = {start: 0}

    while open_list:
        current_node, _ = min(
            open_list,
            key=lambda x: x[1] + heuristic[x[0]]
        )

        open_list.remove(
            (current_node, g_cost[current_node])
        )

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]

            path.append(start)
            path.reverse()

            return path, g_cost[goal]

        for neighbour, cost in graph[current_node]:
            new_cost = g_cost[current_node] + cost

            if neighbour not in g_cost or new_cost < g_cost[neighbour]:
                g_cost[neighbour] = new_cost
                came_from[neighbour] = current_node
                open_list.append((neighbour, new_cost))

    return None, float("inf")


start = input("Enter the start node: ").upper()
goal = input("Enter the goal node: ").upper()

path, cost = astar(start, goal)

if path:
    print("\nShortest path:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("Path not found!")