##Code for Noughts and Crosses game
import os # going to use this to create a function that clears the screen

#Function that clears  the screen in terminal
def clear():
    os.system ('cls')
#Global variables




#assigining values of board    
board = ['#','1','2','3','4','5','6','7','8','9'] # used to display the noughts and crosses board + update

#code to display the board
def displayBoard(board):
    #enumerated_board =enumerate(board)
    

    
    #print(list(enumerated_board))
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print(f"_________\n")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"_________\n")
    print(f"{board[7]} | {board[8]} | {board[9]}")

## Testing the code above ##
testBoard = ['#','X','O','X','O','X','O','X','O','X']
displayBoard(testBoard)

##functio that takes in a player input and assigns their marker as X or O
def playerInput():
    
    #acceptable values
    validInput = ['X','O']
    
    #player grid symbol
    global playerSym # used to take in users chosesn symbol , X or O
    playerSym = 'Z'# should be X or O to exit while
    
    while playerSym not in validInput:
        
        
        
        playerSym= input('Please choose X or O: ')
        
        clear()#avoids long list of incorrect inputs
        
        #error message for incorrect input
        if playerSym not in validInput:
            print(f"{playerSym} is not a valid input, choose X or O")
         
    return playerSym  

## Testing player input 
playerInput()

#Function that takes in the board list object, a player symbol (X or O), and a desired position (number 1-9)
def markerPos():
    
    
    displayBoard(board)
    
    #acceptable values
    validInput = [num for num in range(1,10)]
    
    #player grid symbol
    global gridPos # used to determine where player symbol should be placed
    gridPos = '10'# should be 1 to 9 to exit while
    
    while gridPos not in validInput:
        
        gridPos= int(input('Please choose one grid position from 1 to 9: '))
        
        clear()#avoids long list of incorrect inputs
        
        #error message for incorrect input
        if gridPos not in validInput:
            print(f"{gridPos} is not a valid input, enter new grid position 1 to 9: ")
    
    return gridPos

##Testing MarkerPos function
markerPos()

# Function for placing the players chosen symbol on the board
def placeMarker(board, playerSym, gridPos):
    
    board[gridPos]= playerSym # placing the players symbol on the chosen grid position
    
    return displayBoard(board)

#testing place marker function

placeMarker(board,playerSym,gridPos)

#Function to check whether the placement of a player symbol has won the game

def win_check(board, mark):
    #winning lists
    
    if board[1:4].count(mark)==3 or board[4:7].count(mark)==3 or board[7:10].count(mark)==3:
        status = "You've Won"
    #diagonals
    elif board[1]=='X' and board[5] =='X' and board[9]=='X' or  board[3]=='X' and board[5]=='X' and board[7]=='X':
        status = "You've Won"
    
    else: pass

    return status
#testing win_check function
win_check(board,'O')




