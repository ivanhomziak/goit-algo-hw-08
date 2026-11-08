"""Simple binary search tree implementation shared by tasks 1 and 2.

The tree stores integers. Duplicate values are inserted into the right subtree.
"""

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(slots=True)
class Node:
    value: int
    left: "Node | None" = None
    right: "Node | None" = None


def insert(root: Node | None, value: int) -> Node:
    """Insert a value into a BST and return the (possibly new) root.

    Iterative insertion avoids Python recursion-depth limitations for skewed trees.
    """
    if root is None:
        return Node(value)

    current = root
    while True:
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
                return root
            current = current.left
        else:
            if current.right is None:
                current.right = Node(value)
                return root
            current = current.right


def build_bst(values: Iterable[int]) -> Node | None:
    """Build a BST from values. Empty input produces an empty tree."""
    root: Node | None = None
    for value in values:
        root = insert(root, value)
    return root
