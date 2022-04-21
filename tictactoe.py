


board=["-","-","-",
        "-","-","-",
        "-","-","-",]
gameRunning=True
winner=None
player="0"
def printBoard(board):
    print()
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])

turns=1

while gameRunning:
    printBoard(board)
    if turns==9:
        gameRunning=False
    turns+=1
    