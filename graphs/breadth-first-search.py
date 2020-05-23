# The Breadth First Search (BFS) is an algorithm for traversing or searching tree or graph data structures.
# It explores all the nodes at the present depth before moving on to the nodes at the next depth level.

# Time complexity
# The time complexity of BFS if the entire tree is traversed is O(V)O(V) where V is the number of nodes.
# In the case of a graph, the time complexity is O(V + E)O(V+E) where V is the number of vertexes
# and E is the number of edges.

graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']}


# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]

            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


# bfs_connected_component(graph, 'A')
# returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']
if __name__ == '__main__':
    print(bfs_connected_component(graph, 'A'))
