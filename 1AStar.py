def a_star_algorithm(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g_costs = {start_node: 0}
    parents = {start_node: start_node}

    while open_set:
        current_node = None
        for node in open_set:
            if current_node is None or g_costs[node] + heuristic(node) < g_costs[current_node] + heuristic(current_node):
                current_node = node

        if current_node == stop_node:
            path = []
            while parents[current_node] != current_node:
                path.append(current_node)
                current_node = parents[current_node]
            path.append(start_node)
            path.reverse()
            print('Path found:', path)
            return path

        for (neighbor, weight) in get_neighbors(current_node):
            if neighbor not in open_set and neighbor not in closed_set:
                open_set.add(neighbor)
                parents[neighbor] = current_node
                g_costs[neighbor] = g_costs[current_node] + weight
            else:
                if g_costs[neighbor] > g_costs[current_node] + weight:
                    g_costs[neighbor] = g_costs[current_node] + weight
                    parents[neighbor] = current_node
                    if neighbor in closed_set:
                        closed_set.remove(neighbor)
                        open_set.add(neighbor)

        open_set.remove(current_node)
        closed_set.add(current_node)

    print('Path does not exist!')
    return None

def get_neighbors(node):
    return graph.get(node, [])

def heuristic(node):
    heuristic_values = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return heuristic_values.get(node, float('inf'))

graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'E': [('D', 6)],
    'D': [('G', 1)],
}

# Run the A* algorithm
a_star_algorithm('A', 'G')
