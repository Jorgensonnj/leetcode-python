#!/usr/bin/env python

import time
from typing import List

def myGameOfLife(board: List[List[int]]) -> List[List[int]]:
    height = len(board)
    width = len(board[0])
    new_board = []
    for y in range(height):
        for x in range(width):
            above = board[y - 1][x] if y - 1 >= 0     else 0 # above
            below = board[y + 1][x] if y + 1 < height else 0 # below
            left  = board[y][x - 1] if x - 1 >= 0     else 0 # left
            right = board[y][x + 1] if x + 1 < width  else 0 # right

            top_left     = board[y - 1][x - 1] if y - 1 >= 0     and x - 1 >= 0     else 0 # top_left
            top_right    = board[y - 1][x + 1] if y - 1 >= 0     and x + 1 < width  else 0 # top_right
            bottom_left  = board[y + 1][x - 1] if y + 1 < height and x - 1 >= 0     else 0 # bottom_left
            bottom_right = board[y + 1][x + 1] if y + 1 < height and x + 1 < width  else 0 # bottom_right

            #new_board[y][x] = neighbor_sum
            #print(neighbor_sum)
            neighbor_sum = above + below + left + right + top_left + top_right + bottom_left + bottom_right

            if board[y][x] == 1:
                if neighbor_sum < 2:
                    new_board.append((y,x,0))
                elif 1 < neighbor_sum < 4:
                    new_board.append((y,x,1))
                else:
                    new_board.append((y,x,0))
            else:
                if neighbor_sum == 3:
                    new_board.append((y,x,1))
                else:
                    new_board.append((y,x,0))

    for (j, i, val) in new_board:
        board[j][i] = val

    return board

def otherGameOfLife(board: List[List[int]]) -> List[List[int]]:
    m, n = len(board), len(board[0])

    def count_live_neighbors(i, j):
        count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < m and 0 <= nj < n and (board[ni][nj] == 1 or board[ni][nj] == -1):
                count += 1

        return count

    for i in range(m):
        for j in range(n):
            live_neighbors = count_live_neighbors(i, j)

            if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[i][j] = -1  # Mark as dead (was alive)
            elif board[i][j] == 0 and live_neighbors == 3:
                board[i][j] = 2   # Mark as alive (was dead)

    # Update the board with the next state
    for i in range(m):
        for j in range(n):
            if board[i][j] == -1:
                board[i][j] = 0  # Set dead
            elif board[i][j] == 2:
                board[i][j] = 1  # Set alive

    return board

def main():

    tests = [
        [
            [0,1,0],
            [0,0,1],
            [1,1,1],
            [0,0,0]
        ],
        [
            [1,1],
            [1,0]
        ]
    ]

    for (number, test) in enumerate(tests):
        start_time = time.time()

        my_result = myGameOfLife(test.copy())
        print(
            "Test: " + str(number) +
            " Time: {:10.9f} ".format(time.time() - start_time) +
            " Result:\n" + str(my_result)
        )

        start_time = time.time()
        other_result = otherGameOfLife(test.copy())
        print(
            "Test: " + str(number) +
            " Time: {:10.9f} ".format(time.time() - start_time) +
            " Result:\n" + str(other_result)
        )

if __name__ == "__main__":
    main()
