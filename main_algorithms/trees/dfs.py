def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    # 1. Помечаем узел как посещенный
    visited.add(node)
    print(f"Посетили: {node}")

    # 2. Идем во все соседние узлы, которые еще не видели
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited


def dfs_iterative(graph, start_node):
    visited = set()
    stack = [start_node]  # Стек — LIFO (Last In, First Out)

    while stack:
        node = stack.pop()  # Достаем последний добавленный элемент

        if node not in visited:
            print(f"Посетили: {node}")
            visited.add(node)

            # Добавляем соседей в стек.
            # Чтобы порядок обхода был такой же, как в рекурсии,
            # соседей можно добавить в обратном порядке: reversed(graph[node])
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited