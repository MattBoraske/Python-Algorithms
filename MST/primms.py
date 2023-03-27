'''
Basic idea - start with an arbitary vertex and add its vertexes to a priority queue.
Pop off cheapest edge, add it to the list of edges that make up the MST, and travel to the next node it connects to. Mark that node
as visited and add its nodes to the priority queue. Repeat until all nodes are visited.
After all nodes are visited, the MST is complete.
'''

import heapq
def prim_mst(graph):
    """
    Implementation of Prim's algorithm for finding the minimum spanning tree (MST) of a graph.
    Input: 
    - graph: a dictionary representing the graph as an adjacency list
    Output: 
    - mst: a list of tuples representing the edges in the MST
    """
    # Initialize the MST and the heap
    mst = []
    heap = [(0, 0, None)]
    visited = set()

    # Loop until the heap is empty
    while heap:
        # Pop the minimum cost edge from the heap
        cost, node, parent = heapq.heappop(heap)

        # Check if the node has been visited before
        if node not in visited:
            # Add the node to the visited set and add the edge to the MST
            visited.add(node)
            if parent is not None:
                mst.append((parent, node, cost))

            # Add the neighbors of the node to the heap
            for neighbor, neighbor_cost in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (neighbor_cost, neighbor, node))

    # Return the MST
    return mst

def main():
    # Create a small graph

    graph = {
        0: {1: 2, 2: 3, 3: 1},
        1: {0: 2, 2: 4},
        2: {0: 3, 1: 4, 3: 5},
        3: {0: 1, 2: 5}
    }

    # Compute the MST using prim_mst()
    mst = prim_mst(graph)

    # Print the edges in the MST and the total weight
    print("Minimum Spanning Tree:")
    for edge in mst:
        print(f"{edge[0]} -- {edge[1]} : {edge[2]}")
    total_weight = sum(edge[2] for edge in mst)
    print(f"Total weight: {total_weight}")

if __name__ == '__main__':
    main()
