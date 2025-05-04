# Define the decision tree as a dictionary
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}


def dfs_recursive(tree, node, visited=None):
    """
    Recursive DFS function
    """
    if not visited:
        visited = set()  # Initialize the visited set
    visited.add(node)    # Mark the node as visited

    for child in tree[node]:  # Recursively visit children
        if child not in visited:
            dfs_recursive(tree, child, visited)

    return visited


def dfs_iterative(tree, start):
    """
    Iterative DFS function
    """
    visited = set()  # Track visited nodes
    stack = [start]  # Stack for DFS

    while stack:  # Continue until stack is empty
        node = stack.pop()  # Pop a node from the stack
        if node not in visited:
            visited.add(node)  # Mark node as visited
            print(node)        # Print the current node (for illustration)
            stack.extend(reversed(tree[node]))  # Add child nodes to stack

    return visited


if __name__ == "__main__":
    recursive_nodes = dfs_recursive(tree, 'D')
    iterative_nodes = dfs_iterative(tree, 'A')
    
