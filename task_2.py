"""Task 2: Calculate the sum of all values in a BST."""

from bst import Node, build_bst


def sum_tree(root: Node | None) -> int:
    """Return the sum of all node values (0 for an empty tree).

    Depth-first traversal visits each node exactly once. An explicit stack
    avoids RecursionError for deeply skewed BSTs.

    Time complexity: O(n), where n is the number of nodes.
    Extra space: O(h), where h is the height of the tree.
    """
    if root is None:
        return 0

    total = 0
    stack = [root]

    while stack:
        current = stack.pop()
        total += current.value
        if current.left is not None:
            stack.append(current.left)
        if current.right is not None:
            stack.append(current.right)

    return total


if __name__ == "__main__":
    values = [10, 5, 15, 3, 7, 12, 18]
    tree = build_bst(values)
    print(f"BST values: {values}")
    print(f"Sum of all values: {sum_tree(tree)}")  # 70
