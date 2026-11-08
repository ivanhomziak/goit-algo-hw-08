"""Task 1: Find the smallest value in a binary search tree (BST)."""

from bst import Node, build_bst


def find_min(root: Node | None) -> int | None:
    """Return the smallest value in a BST, or None for an empty tree.

    In a BST, every value in a left subtree is less than its parent value.
    Therefore, the leftmost node contains the minimum.

    Time complexity: O(h), where h is the height of the tree.
    Extra space: O(1).
    """
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left
    return current.value


if __name__ == "__main__":
    values = [10, 5, 15, 3, 7, 12, 18]
    tree = build_bst(values)
    print(f"BST values: {values}")
    print(f"Minimum value: {find_min(tree)}")  # 3
