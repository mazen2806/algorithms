from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph1(start_node: Optional['Node']):
    graph_clone = {}

    def dfs(node):
        if node in graph_clone:
            return graph_clone[node]

        copy = Node(node.val)
        graph_clone[node] = copy

        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(start_node) if start_node else None


def clone_graph2(start_node: Optional['Node']) -> Optional['Node']:
    if not start_node:
        return None

    def clone_graph(node, seen={}):
        if node in seen:
            return seen[node]

        cloned_node = Node(node.val)
        seen[node] = cloned_node

        for neighbor in node.neighbors:
            cloned_neighbor = clone_graph(neighbor, seen)
            cloned_node.neighbors.append(cloned_neighbor)

        return cloned_node
    return clone_graph(start_node)
