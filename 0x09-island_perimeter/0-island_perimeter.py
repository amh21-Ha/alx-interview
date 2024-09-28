#!/usr/bin/python3
"""
Function to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    perimeter = 0

    # Get the number of rows and columns
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Iterate through the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 edges for each land cell
                perimeter += 4

                # Check the left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Reduce by 2 for the shared ed

                # Check the top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Reduce by 2 for the shared edge

    return perimeter
