def display(board):
    for i in board:
        for element in i:
            if element:
                print("K",end=" ")
            else:
                print("X",end=" ")
        print()
def isValid(board,r,c):
    if r>=0 and r<len(board) and c>=0 and c<len(board):
        return True
    return False
def isSafe(board,r,c):
    if isValid(board,r-2,c-1):
        if board[r-2][c-1]:
            return False
    if isValid(board,r-2,c+1):
        if board[r-2][c+1]:
            return False
    if isValid(board,r-1,c+2):
        if board[r-1][c+2]:
            return False
    if isValid(board,r-1,c-2):
        if board[r-1][c-2]:
            return False
    return True


def knights(board,r,c,target):
    if target==0:
        display(board)
        print()
        return 1
    if r==len(board)-1 and c==len(board):
        return
    if c==len(board):
        knights(board,r+1,0,target)
        return
    if isSafe(board,r,c):
        board[r][c]=True
        knights(board,r,c+1,target-1)
        board[r][c]=False
    #if it doesnot safe then dont reduce the knights
    knights(board,r,c+1,target)

board=[[False,False,False,False],
[False,False,False,False],
[False,False,False,False],
[False,False,False,False]]
knights(board,0,0,4)
