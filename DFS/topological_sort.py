from collections import defaultdict, deque

def topological_sort(graph):
    # Compute the in-degree of each node
    in_degree = defaultdict(int)
    for u in graph:
        for v, weight in graph[u]:
            in_degree[v] += weight

    # Initialize the queue with nodes with zero in-degree
    queue = deque(u for u in graph if in_degree[u] == 0)

    # Initialize the topological order
    topological_order = []

    # Perform the topological sort
    while queue:
        u = queue.popleft()
        topological_order.append(u)
        for v, weight in graph[u]:
            in_degree[v] -= weight
            if in_degree[v] == 0:
                queue.append(v)

    # Check if the graph is a DAG
    if len(topological_order) != len(graph):
        raise ValueError("Graph contains a cycle")

    return topological_order

def main():
    # Example weighted DAG
    graph = {
        'A': [('B', 3), ('C', 2)],
        'B': [('C', 1)],
        'C': [('D', 4)],
        'D': []
    }

    # Perform the topological sort
    try:
        order = topological_sort(graph)
        print("Topological order:", order)
    except ValueError as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()