class TTTBoard:
    def __init__(self):
        #Empty board
        self.board = [['_' for _ in range(3)] for _ in range(3)]

    #Set the board to a specific position
    def setBoard(self, board):
        self.board = board

    #Print board
    def printBoard(self):
        for i in self.board:
            print(i)

    #Restart the board
    def resetBoard(self):
        self.board = [['_' for _ in range(3)] for _ in range(3)]

    #Update a position in the board
    def update(self, turn, y, x):
        self.board[y][x] = turn

    #Check if someone won and if so, return the coordinates of the buttons
    def checkIfWon(self):
        for i in range(3):
            if self.board[i][0] != '_' and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0], [[i, 0], [i, 1], [i,2]]
            elif self.board[0][i] != '_' and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i], [[0, i], [1, i], [2, i]]

        if self.board[1][1] != '_' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[1][1], [[0, 0], [1, 1], [2, 2]]
        elif self.board[1][1] != '_' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[1][1], [[0, 2], [1, 1], [2, 0]]
        
        #If nobody won, check if there's still are any available positions
        for i in self.board:
            if ('_' in i) == True:
                #If there's an available box, return None
                return None, None
        
        #If nobody won and there isn't any available box, return 'T' for tie
        return 'T', None

    #Return the current board
    def getCurrentBoard(self):
        return self.board