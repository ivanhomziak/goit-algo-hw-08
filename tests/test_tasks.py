"""Standard-library unit tests for homework 08."""

import random
import unittest
from functools import lru_cache
from itertools import combinations

from bst import Node, build_bst, insert
from task_1 import find_min
from task_2 import sum_tree
from task_3 import minimum_connection_cost, optimal_connection_plan


class TestBST(unittest.TestCase):
    def test_minimum_in_example(self) -> None:
        self.assertEqual(find_min(build_bst([10, 5, 15, 3, 7, 12, 18])), 3)

    def test_minimum_with_negative_values_and_duplicates(self) -> None:
        self.assertEqual(find_min(build_bst([0, -10, 5, -10, 7])), -10)

    def test_minimum_of_single_node(self) -> None:
        self.assertEqual(find_min(Node(42)), 42)

    def test_empty_tree_minimum(self) -> None:
        self.assertIsNone(find_min(None))

    def test_sum_of_example(self) -> None:
        self.assertEqual(sum_tree(build_bst([10, 5, 15, 3, 7, 12, 18])), 70)

    def test_sum_with_negative_values_and_duplicates(self) -> None:
        self.assertEqual(sum_tree(build_bst([3, -2, -2, 5])), 4)

    def test_empty_tree_sum(self) -> None:
        self.assertEqual(sum_tree(None), 0)

    def test_unbalanced_tree_does_not_overflow_recursion(self) -> None:
        values = range(1200)
        root = build_bst(values)
        self.assertEqual(find_min(root), 0)
        self.assertEqual(sum_tree(root), sum(values))

    def test_insert_preserves_existing_root(self) -> None:
        root = Node(10)
        self.assertIs(insert(root, 7), root)
        self.assertEqual(root.left.value, 7)


@lru_cache(maxsize=None)
def brute_force_minimum_cost(cables: tuple[int, ...]) -> int:
    """Exhaustively enumerate merge orders for small inputs (test oracle)."""
    if len(cables) < 2:
        return 0
    best = float("inf")
    for i, j in combinations(range(len(cables)), 2):
        combined = cables[i] + cables[j]
        remaining = [cables[k] for k in range(len(cables)) if k not in (i, j)]
        remaining.append(combined)
        next_cost = combined + brute_force_minimum_cost(tuple(sorted(remaining)))
        best = min(best, next_cost)
    return int(best)


class TestCables(unittest.TestCase):
    def test_example(self) -> None:
        self.assertEqual(minimum_connection_cost([4, 3, 2, 6]), 29)

    def test_optimal_plan(self) -> None:
        total, steps = optimal_connection_plan([4, 3, 2, 6])
        self.assertEqual(total, 29)
        self.assertEqual(steps, [(2, 3, 5), (4, 5, 9), (6, 9, 15)])
        self.assertEqual(sum(step[2] for step in steps), total)

    def test_no_or_one_cable(self) -> None:
        self.assertEqual(minimum_connection_cost([]), 0)
        self.assertEqual(minimum_connection_cost([50]), 0)

    def test_duplicates_and_zero(self) -> None:
        self.assertEqual(minimum_connection_cost([0, 0, 1]), 1)
        self.assertEqual(minimum_connection_cost([5, 5, 5]), 25)

    def test_invalid_inputs(self) -> None:
        for cables in ([1, -2], [2.5, 3], [True, 3], ["5", 3]):
            with self.subTest(cables=cables):
                with self.assertRaises(ValueError):
                    minimum_connection_cost(cables)

    def test_input_not_modified(self) -> None:
        values = [5, 3, 4]
        minimum_connection_cost(values)
        self.assertEqual(values, [5, 3, 4])

    def test_greedy_matches_brute_force(self) -> None:
        rng = random.Random(42)
        for size in range(0, 7):
            for _ in range(16):
                values = [rng.randint(0, 20) for _ in range(size)]
                with self.subTest(values=values):
                    self.assertEqual(
                        minimum_connection_cost(values),
                        brute_force_minimum_cost(tuple(sorted(values))),
                    )


if __name__ == "__main__":
    unittest.main()
