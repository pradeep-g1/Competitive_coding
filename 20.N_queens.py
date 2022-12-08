def display(board):
    for i in board:
        for element in i:
            if element:
                print("Q",end=" ")
            else:
                print("X",end=" ")
        print()
def isSafe(board,r,col):
    #check vertical row
    for i in range(r):
        if board[i][col]:
            return False
    #diagonal left
    maxleft=min(r,col)
    for i in range(1,maxleft+1):
        if board[r-i][col-i]:
            return False
    #daigonal right
    maxright=min(r,len(board)-col-1)
    for i in range(1,maxright+1):
        if board[r-1][col+1]:
            return False
    return True
def queens(board,r):
    if r==len(board):
        display(board)
        print()
        return 1
    #placing the queen and checking for every row and column
    count=0
    for col in range(len(board)):
        #place the queen if it is safe
        if isSafe(board,r,col):
            board[r][col]=True
            count+=queens(board,r+1)
            board[r][col]=False
    return count

board=[[False,False,False,False,False],
[False,False,False,False,False],
[False,False,False,False,False],
[False,False,False,False,False],
[False,False,False,False,False]]
print(queens(board,0))