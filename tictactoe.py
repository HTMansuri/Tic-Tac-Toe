"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None
start = X


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_nonempty = sum(1 for row in board for cell in row if cell is not EMPTY)
    if num_nonempty % 2 == 0:
        return X
    else:
        return O    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                actions.add((row, col))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result_board = copy.deepcopy(board)
    currplayer = player(board)
    i = action[0]
    j = action[1]
    if result_board[i][j] != EMPTY:
        raise RuntimeError("Invalid Action")
    else:
        result_board[i][j] = currplayer
    return result_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) != EMPTY or all(all(cell is not EMPTY for cell in row) for row in board)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return EMPTY
    do = EMPTY
    if player(board) == O:
        v = float('inf')   
        for action in actions(board):
                tempV = min(v, MAXVALUE(result(board, action)))
                if tempV < v:
                    v = tempV
                    do = action
        return do
    else:
        v = float('-inf')
        for action in actions(board):
            tempV = max(v, MINVALUE(result(board, action)))
            if tempV > v:
                v = tempV
                do = action
        return do

def MINVALUE(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, MAXVALUE(result(board, action)))
    return v

def MAXVALUE(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, MINVALUE(result(board, action)))
    return v
