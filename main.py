def count_power_groups(stations, lines):
    """
    Count how many connected groups of power stations exist.

    stations: list of station name strings.
    lines: list of (a, b) pairs, meaning there is an undirected line between a and b.

    Return: integer number of connected components (groups) in the network.
    """

    # Step 1–3: Understand problem: connected components in an undirected graph
    # Input: list of stations, list of (a,b) lines
    # Output: integer count of connected groups

    # Step 4: Build adjacency list for graph representation
    graph = {s: set() for s in stations}

    for a, b in lines:
        graph[a].add(b)
        graph[b].add(a)

    visited = set()
    groups = 0

    # Step 5–6: Traverse graph with DFS/BFS and count components
    for station in stations:
        if station not in visited:
            groups += 1
            # BFS or DFS — here we use a stack-based DFS
            stack = [station]
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            stack.append(neighbor)

    return groups
