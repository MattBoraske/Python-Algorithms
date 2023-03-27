'''
Basic idea - Grow MST by greedily adding the cheapest edges that don't create a cycle.
This can be interpreted as the edges being in disjoint sets and thus Kruskal's is
an implementation of the union-find algorithm.
'''

from disjoint_set import DisjointSet
def kruskals(edges):
    """
    Implementation of Kruskal's algorithm for finding the minimum spanning tree (MST) of a graph.
    Input: 
    - edges: a list of tuples representing the edges in the graph
    Output: 
    - mst: a list of tuples representing the edges in the MST
    """
    # Initialize the MST and the disjoint set
    mst = []
    disjoint_set = DisjointSet()

    # Sort the edges by cost
    edges.sort(key=lambda x: x[2])

    # Loop through the edges
    for edge in edges:
        # Get the nodes and the cost of the edge
        node1, node2, cost = edge

        # Check if the nodes are in the same set
        if disjoint_set.find(node1) != disjoint_set.find(node2):
            # Add the edge to the MST
            mst.append(edge)

            # Union the sets
            disjoint_set.union(node1, node2)

    # Return the MST
    return mst

def main():
    # Create a small graph
    edges = [
        (0, 1, 8),
        (0, 2, 10),
        (0, 3, 4),
        (1, 2, 1),
        (2, 3, 3)
    ]

    # Compute the MST using kruskals()
    mst = kruskals(edges)

    # Print the edges in the MST and the total weight
    print("Minimum Spanning Tree:")
    for edge in mst:
        print(f"{edge[0]} -- {edge[1]} : {edge[2]}")
    total_weight = sum(edge[2] for edge in mst)
    print(f"Total weight: {total_weight}")

if __name__ == '__main__':
    main()