import os
import time

from utils import (
    constrain,
    print_board,
)


INITIAL_BOARD = {
    (2, 20),
    (3, 18), (3, 20),
    (4, 8), (4, 9), (4, 16), (4, 17),
    (5, 7), (5, 11), (5, 16), (5, 17),
    (7, 2), (7, 3), (7, 6), (7, 10), (7, 12), (7, 13), (7, 18), (7, 20),
    (8, 6), (8, 12), (8, 20),
    (9, 7), (9, 11),
    (10, 8), (10, 9)
}


def get_neighbors_of(cell):
    x, y = cell
    topleft = (x-1,y-1)
    topmid = (x-1,y+0)
    topright = (x-1,y+1)
    midleft = (x+0,y-1)
    midright =(x+0,y+1)
    bottomleft =(x+1,y-1)
    bottommid =(x+1,y+0)
    bottomright=(x+1,y+1)
    neighbors = {topleft,topmid,topright,
                midleft,midright,
                bottomleft,bottommid,bottomright}
    return neighbors

def over3_neighbors_die(board, cell):
    neighbors = 0
    count = 0
    neighbor_cells = get_neighbors_of(cell)
    for item in board:
        if item in neighbor_cells:
            count += 1

    if count > 3:
        board.remove(cell)

    return board



def advance(board):
    """
    Advance the board one step and return it.
    """
    new_board = set()
    for cell in board:
        # your code below
        pass

    return new_board


def start(board, steps=100, size=20):
    for i in range(1, steps + 1):
        os.system('clear')
        print('step:', i, '/', steps)
        print_board(board, size)
        time.sleep(0.1)
        board = constrain(advance(board), size)


if __name__ == '__main__':
    start(INITIAL_BOARD)
