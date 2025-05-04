import pytest
from graphs.dfs import dfs_recursive, dfs_recursive


TREE = {
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

def test_dfs_recursive():
    result = dfs_recursive(TREE, 'D')
    assert result, ['D','H', 'I']


def test_dfs_recursive_with_empty_nodes():
    result = dfs_recursive(TREE, 'F')
    assert result, []

def test_dfs_iterative():
    result = dfs_recursive(TREE, 'A')
    assert result, {'H', 'D', 'G', 'J', 'N', 'E', 'B', 'O', 'A', 'I', 'C', 'L', 'M', 'K', 'F'}
