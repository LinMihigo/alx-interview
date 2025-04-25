#!/usr/bin/python3
"""
lockboxes' Task 0
"""
from typing import List


def canUnlockAll(boxes: List) -> bool:
    """Determines if all boxes can be opened
    """
    n = len(boxes)
    visited = set([0])
    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == n
