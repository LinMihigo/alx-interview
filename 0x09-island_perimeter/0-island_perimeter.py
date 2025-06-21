#!/usr/bin/python3


def island_perimeter(grid):
    """
    Returns the perimeter of the island in the grid.
    :param grid: List[List[int]] where 1 = land and 0 = water
    :return: int - perimeter of the island
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                # If the land cell above is also land, subtract 2 (shared edge)
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                # If the land cell to the left is also land, subtract 2
                # (shared edge)
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
