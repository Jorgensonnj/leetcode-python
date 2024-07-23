#!/usr/bin/env python

import time

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """

    count = 0
    visited = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '1':
                if is_island(grid, y, x, visited):
                    #print("Y: " + str(y) + " X: " + str(x))
                    count += 1

    return count

def is_island(grid, row, column, visited):
    row_inbounds    = 0 <= row    and row    < len(grid)
    column_inbounds = 0 <= column and column < len(grid[0])
    if not row_inbounds or not column_inbounds:
        return False

    if grid[row][column] == '0':
        return False

    postion = str(row) + str(column)

    if postion in visited:
        return False

    visited.add(postion)

    is_island(grid, row - 1, column,     visited)
    is_island(grid, row + 1, column,     visited)
    is_island(grid, row,     column - 1, visited)
    is_island(grid, row,     column + 1, visited)

    return True


def main():

    tests = [
        [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ],
        [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
    ]

    for (number, test) in enumerate(tests):
        start_time = time.time()
        result = numIslands(test)
        print(
            "Test: " + str(number) +
            " Result: " + str(result) +
            " Time: {:10.9f}".format(time.time() - start_time)
        )


if __name__ == "__main__":
    main()
