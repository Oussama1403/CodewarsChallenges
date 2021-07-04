def is_solved(board):
    
    for row in board:
        if len(set(row)) == 1:
            if row[0] == 1:
                return 1
            elif row[0] == 2:
                return 2
    
    #check board[0][0],board[1][1] and board[2][2]
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        if board[0][0] == 1:
            return 1
        elif board[0][0] == 2:
            return 2
    #check board[0][2],board[1][1] and board[2][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        if board[0][len(board)-1] == 1:
            return 1
        elif board[0][len(board)-1] == 2:
            return 2
    #check board[0][1],board[1][1] and board[2][1]
    if len(set([board[i][1] for i in range(len(board))])) == 1:
        if board[0][1] == 1:
            return 1
        elif board[0][1] == 2:
            return 2

    for l in range(len(board)):
        for c in range(len(board)):
            if board[l][c] == 0:
                return -1
    
    return 0