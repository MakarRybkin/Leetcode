from collections import deque


def bfs(graph, start_node):
    queue = deque([start_node])
    visited = {start_node}  # Чтобы не ходить кругами

    while queue:
        node = queue.popleft()  # Достаем первого в очереди
        print(f"Посетили узел: {node}")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)  # Добавляем соседей в конец очереди


