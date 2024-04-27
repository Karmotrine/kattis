player_1 = {
    "name": "Jebb",
    "symbol": 'O'
}

BOARD_SZ = 3
board = [[] for i in range(BOARD_SZ)]
for i in range(BOARD_SZ):
    board[i] = list(input())

def check_row(board: list, player: dict):
    for i in range(BOARD_SZ):
        if "".join([x for x in board[i]]) == BOARD_SZ * player['symbol']:
            return True

def check_col(board: list, player: dict) -> bool:
    for i in range(BOARD_SZ):
        current_col = ""
        for j in range(BOARD_SZ):
            current_col += board[j][i]
        if current_col == BOARD_SZ * player['symbol']:
            return True

def check_dia(board:list, player: dict) -> bool:
    LR_dia = ""
    for i in range(BOARD_SZ):
        LR_dia += board[i][i]
    RL_dia = ""
    for j in range(BOARD_SZ):
        RL_dia += board[j][BOARD_SZ - 1 - j]
    if LR_dia == BOARD_SZ * player['symbol']:
        return True
    if RL_dia == BOARD_SZ * player['symbol']:
        return True

def check_win(board: list, player: dict) -> bool:
    return (
        check_row(board, player_1) or 
        check_col(board, player_1) or
        check_dia(board, player_1)
    )

print("Jebb" if check_win(board, player_1) else "Neibb")