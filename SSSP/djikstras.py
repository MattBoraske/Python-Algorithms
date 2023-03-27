import heapq

'''
Basic idea - Use priority queue to greedily always visit the next node with shortest distance.
Shortest distances will be found once priority queue is empty
'''
def djikstras(graph, start):
    """
    Dijkstra's algorithm for finding shortest paths in a weighted graph.

    Parameters:
    graph (dict): A dictionary representing the weighted graph.
    start (any): The starting node for the algorithm.

    Returns:
    A tuple containing two dictionaries:
    - shortest_distances: A dictionary mapping each node to its shortest distance from the start node.
    - previous_nodes: A dictionary mapping each node to its previous node on the shortest path from the start node.
    """
    #shortest distances dict
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0

    #previous nodes dict
    previous_nodes = {node: None for node in graph}

    #priority queue to track nodes to visit
    to_visit = [(0, start)]

    #while priority queue is not empty
    while to_visit:
        #pop off queue to get next node and distance to it
        current_distance, current_node = heapq.heappop(to_visit)
        #get current nodes neighbors and the weights of the edges to them
        for neighbor, weight in graph[current_node].items():
            #calculate distance to the neighbor from current node
            distance = current_distance + weight
            #if this new distance is the shortest distance found so far
            # 1. update shortest distance for neighbor
            # 2. update previous node for neighbor to be current node
            # 3. push neighbor and its new distance to the priority queue
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(to_visit, (distance, neighbor))

    #return tuple of shortest distances and previous nodes dictionaries
    return shortest_distances, previous_nodes

def main():
    graph = {
        '1': {'3':6, '4':3},
        '2': {'1':3},
        '3': {'4':2},
        '4': {'2':1, '3':1},
        '5': {'2':4, '4':2}
    }
    start = '1'
    shortest_distances, previous_nodes = djikstras(graph, start)
    print(f'Shortest path from {start} to...')
    for target_node in previous_nodes.keys():
        if target_node == start:
            continue
        path = []
        if previous_nodes[target_node] == None:
            print(f'\t{target_node}: Does Not Exist')
            continue
        else:
            path = []
            key = target_node
            while target_node:
                path.insert(0, target_node)
                target_node = previous_nodes[target_node]
            path = '->'.join(path)
            print(f'\t{path[-1]}: {path}. Distance = {shortest_distances[key]}')
        
if __name__ == '__main__':
    main()
