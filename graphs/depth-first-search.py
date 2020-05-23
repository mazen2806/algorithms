# The Depth First Search (DFS) is an algorithm for traversing or searching tree or graph data structures which uses the
# idea of backtracking. It explores all the nodes by going forward if possible or uses backtracking.

# Time complexity
# The time complexity of DFS if the entire tree is traversed is O(V)O(V) where V is the number of nodes.
# In the case of a graph, the time complexity is O(V + E)O(V+E) where V is the number of vertexes
# and E is the number of edges.

# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

# Set to keep track of visited nodes.
visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


if __name__ == "__main__":
    dfs(visited, graph, 'A')
