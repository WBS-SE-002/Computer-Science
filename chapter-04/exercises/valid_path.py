from collections import defaultdict, deque

def validPath(n, edges, source, destination):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    seen = [False] * n
    seen[source] = True
    queue = deque([source])

    while queue:
        curr_node = queue.popleft()

        if curr_node == destination:
            return True

        for next_node in graph[curr_node]:
            if not seen[next_node]:
                seen[next_node] = True
                queue.append(next_node)
    return False

print(validPath(3, [[0,1], [1,2], [2,0]], 0, 2))