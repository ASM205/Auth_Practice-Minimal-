from tkinter import *


tk = Tk()
tk . title('Tic-Tac-Toe')

# create buttons with variable board
#player = 1
win = 1
draw = -1
run = 0
stop = 1
board = [' 'for _ in range(10)]
game = run
mark = 'X'
def checkWin():
    global game
    win_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), # Rows
                      (1, 4, 7), (2, 5, 8), (3, 6, 9), # Columns
                      (1, 5, 9), (3, 5, 7)]            # Diagonals

    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            game = win
            return
    
    if all(space != ' ' for space in board[1:]):
        game = draw
    else:
        game = run

def drawBoard(): # change this to gui board
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('___|___|___')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('___|___|___')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    
def checkPosition(x):
    if board[x] == ' ':
        return True
    else:
        return False

#print("Tic-Tac-Toe Game")
label = Label(tk, text = "Player 1 [X] --- Player 2 [O]") #print this as message - 
label.pack()
#print("Please Wait...")

player = 1
while game == run:
        
    drawBoard()
    if player % 2 != 0:
        turn = Message(tk, text = "Player 1's chance")
        Mark = 'X'
    else:
        turn = Message(tk, text = "Player 2's chance")
        Mark = 'O'
    turn.pack()
    try:
        choice = int(input("Enter the position between [1-9] where you want to mark: ")) #select using buttons
    except ValueError:
        validity = Message(tk, text = "Invalid input. Please enter a number between 1 and 9.")
        continue

    if choice < 1 or choice > 9:
        validity = Message(tk, text = "Invalid input. Please enter a number between 1 and 9.")
        continue

    if checkPosition(choice):
        board[choice] = Mark #button configure text = mark
        player += 1
        checkWin()
    else:
        validity = Message(tk, text = "Position already occupied. Try again.")
    validity.pack()
    
    if game == draw:
        print("Game Draw")
    elif game == win:
        player -= 1
        if player % 2 != 0:
            winner = Message(tk, text = "Player 1 Won")
        else:
            winner = Message(tk , text = "Player 2 Won")
        winner.pack()


tk.mainloop()