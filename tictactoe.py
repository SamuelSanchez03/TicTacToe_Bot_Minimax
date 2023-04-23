from tkinter import *
from tkinter import messagebox
from TTTBoard import TTTBoard
from bot import Bot

root = Tk()
board = TTTBoard()
buttons = [[0 for _ in range(3)] for _ in range(3)]
bot = Bot()

#Disable all buttons
def disableButtons():
    global buttons
    for i in buttons:
        for j in i:
            j.config(state=DISABLED)

#Change color in the winning buttons
def winningButtons(coords):
    global buttons

    for i in coords:
        buttons[i[0]][i[1]].config(bg="red")

#Button clicked function
def buttonClicked(b, y, x):
    global board, bot, buttons
    
    #If button hasn't been pressed
    if b["text"] == " ":
        b["text"] = "X"                                             #Change label
        board.update('X', y, x)                                     #Update board of the game
        b.config(state=DISABLED)                                    #Disable button
        winner, coords = board.checkIfWon()                         #Check if someone won

        #If the human won
        if winner == 'X':
            winningButtons(coords)                                  #Change the color of the buttons
            disableButtons()                                        #Disable all the buttons
            messagebox.showinfo("Tic Tac Toe", winner + " Wins!")   #Show a message with the winner
            return
        
        #If there's no winner
        elif winner is None:
            botMove = bot.bestMoveAB(board.getCurrentBoard())       #Get the best move from the bot
            buttons[botMove[0]][botMove[1]]["text"] = "O"           #Update the label of the button from the move
            buttons[botMove[0]][botMove[1]].config(state=DISABLED)  #Disable the button
            board.update('O', botMove[0], botMove[1])               #Update the board of the game
            winner, coords = board.checkIfWon()                     #Check if someone won
    
    #If the bot won
    if winner == 'O':
        winningButtons(coords)                                      #Change the color of the buttons
        disableButtons()                                            #Disable all the buttons
        messagebox.showinfo("Tic Tac Toe", winner + " Wins!")       #Show a message with the winner

    #If checkIfWon returns a T is a Tie
    if winner == 'T':                                              
        disableButtons()                                            #Disable all the buttons
        messagebox.showinfo("Tic Tac Toe", "Tie!")                  #Show a message 

    #board.printBoard()

#Start the game
def resetGame():
    global buttons, board

    #Initial conditions
    board.resetBoard()
    #Button array
    for i in range(0, 3):
        for j in range(0, 3):
            buttons[i][j] = Button(root, text=" ", font=("Helvetica", 20), height=6, width=12, bg="SystemButtonFace", command=lambda y=i, x=j: buttonClicked(buttons[y][x], y, x))
            buttons[i][j].grid(row=i, column=j)

#Menu to restart game
myMenu = Menu(root, tearoff=False)
root.config(menu=myMenu)
options = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label="Options", menu=options)
options.add_command(label="Reset game", command=resetGame)

#Start of the app and some configuration
resetGame()
root.title("Tic Tac Toe")
root.resizable(False, False)
root.mainloop()