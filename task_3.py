"""Task 3: Connect network cables with the minimum total cost using a min-heap."""

from collections.abc import Iterable
from heapq import heapify, heappop, heappush


def optimal_connection_plan(
    lengths: Iterable[int],
) -> tuple[int, list[tuple[int, int, int]]]:
    """Return the minimum total cost and the optimal connection steps.

    Each step is (first_cable_length, second_cable_length, resulting_length).
    Cable lengths must be non-negative integers.

    Greedy strategy: always join the two shortest available cables.
    Time complexity: O(n log n); extra space: O(n).
    """
    heap = list(lengths)
    if any(type(length) is not int or length < 0 for length in heap):
        raise ValueError("Cable lengths must be non-negative integers")

    heapify(heap)
    total_cost = 0
    steps: list[tuple[int, int, int]] = []

    while len(heap) > 1:
        first = heappop(heap)
        second = heappop(heap)
        connected = first + second

        total_cost += connected
        steps.append((first, second, connected))
        heappush(heap, connected)

    return total_cost, steps


def minimum_connection_cost(lengths: Iterable[int]) -> int:
    """Return just the minimum possible total connection cost."""
    total_cost, _ = optimal_connection_plan(lengths)
    return total_cost


if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    total_cost, steps = optimal_connection_plan(cables)
    print(f"Cable lengths: {cables}")
    for first, second, connected in steps:
        print(f"Connect {first} + {second} = {connected} (cost: {connected})")
    print(f"Minimum total cost: {total_cost}")  # 29
