from Players import PlayerOne as P1,PlayerTwo as P2


board=["-","-","-","-","-","-","-","-","-"]

gameRunning=True
#all spaces have been changed -
# we have a winner
PlayerOne=P1()
PlayerTwo=P2()
currentPlayer=PlayerOne.name()

i=0
def printoard(board):
    print()
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("-"*9)
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("-"*9)
    print(board[6]+" | "+board[7]+" | "+board[8])


def confirmHor(board):
    if board[0]==board[1]==board[2] and board[2]!="-":
        return True
    if board[3]==board[4]==board[5] and board[5]!="-":
        return True
    if board[6]==board[7]==board[8] and board[2]!="-":
        return True

def confirmVert(board):
     if board[0]==board[3]==board[6] and board[6]!="-":
        return True
     if board[1]==board[4]==board[7] and board[4]!="-":
        return True
     if board[2]==board[5]==board[2] and board[8]!="-":
        return True
def confirmDiag(board):
     if board[0]==board[8]==board[4] and board[8]!="-":
        return True
     if board[6]==board[4]==board[2] and board[4]!="-":
        return True

def checkwin():
   if confirmHor(board) or confirmVert(board) or confirmDiag(board):
        global gameRunning
        gameRunning=False 
def checkTie(board):
    if "-" not in board:
        print("It's a Tie")
        global gameRunning
        gameRunning=False 

def playGame():
    global currentPlayer
    if currentPlayer==PlayerTwo.name():
        currentPlayer=PlayerOne.name()
        userInput=int(input("Provide a value from 1-9"))
        board[userInput-1]=PlayerOne.play()
    else:
        currentPlayer=PlayerTwo.name()
        userInput=int(input("Provide a value from 1-9"))
        board[userInput-1]=PlayerTwo.play()


  
        
while gameRunning:
    printoard(board)
    playGame()
    checkwin()
    checkTie(board)

printoard(board)
  



