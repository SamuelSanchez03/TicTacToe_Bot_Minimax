from TTTBoard import TTTBoard
import math

class Bot:
    def __init__(self):
        self.scores = {'X' : -10, 'O' : 10, 'T': 0}

    #bestMove without optimization
    def bestMove(self, currentBoard):
        #Copy the board
        board = [row[:] for row in currentBoard]
        #Set bestScore to a very small value
        bestScore = -math.inf

        #For every possible move
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    #Put 'O' in the available position
                    board[i][j] = 'O'

                    #Call minimax to see how good the move is
                    #isMaximizing is false because it would be the human's turn
                    score = self.minimax(board, 0, False)

                    #Undo the change to the board
                    board[i][j] = '_'

                    #If the score is bigger than the current best score
                    if score > bestScore:
                        #Set bestScore to score and save the move
                        bestScore = score
                        move = [i, j]

        #After we checked every move, return the best one
        return move
    
    #bestMove with optimization
    def bestMoveAB(self, currentBoard):
        #Copy the board
        board = [row[:] for row in currentBoard]
        #Set bestScore to a very small value
        bestScore = -math.inf

        #For every possible move
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    #Put 'O' in the available position
                    board[i][j] = 'O'

                    #Call minimax to see how good the move is
                    #isMaximizing is false because it would be the human's turn
                    #Set alpha to a very small value and beta to a very large one
                    score = self.minimaxAB(board, 0, -math.inf, math.inf, False)

                    #Undo the change to the board
                    board[i][j] = '_'

                    #If the score is bigger than the current best score
                    if score > bestScore:
                        #Set bestScore to score and save the move
                        bestScore = score
                        move = [i, j]

        #After we checked every move, return the best one
        return move

    #Vanilla minimax
    def minimax(self, currentBoard, depth, isMaximizing):
        #Copy the board
        board = [row[:] for row in currentBoard]

        #Evaluate the current position
        result = self.evaluatePosition(board)

        #If someone won or there is a tie
        if result != None:
            #Set eval to the value of the result in the dictionary
            eval = self.scores[result]

            #If is a tie, return 0
            if eval == 0:
                return eval
            
            #If the bot won, return the evaluation minus the depth, we want the fastest way to win
            #If the human won, return the evaluation plus the depth, the human would want the fastest win
            return eval - depth if eval > 0 else eval + depth

        #When is the bot's turn
        if isMaximizing:
            #Set maxEval to a very small value
            maxEval = -math.inf

            #For every possible position in the board
            for i in range(3):
                for j in range(3):
                    #If the box is empty
                    if(board[i][j] == '_'):
                        #Put 'O' in the position
                        board[i][j] = 'O'

                        #New call to the minimax function with the new position
                        #Add one to the depth to know how many moves have been done
                        #isMaximizing is false because it would be the human's turn
                        eval = self.minimax(board, depth + 1, False)

                        #Undo the move
                        board[i][j] = '_'

                        #Set maxEval to the maximum between the current maxEval and the eval minimax returned
                        maxEval = max(maxEval, eval)

            #After all the moves, return the maxEval
            return maxEval    

        else:
            #Set minEval to a very large value
            minEval = math.inf

            #For every possible position in the board
            for i in range(3):
                for j in range(3):
                    #If the box is empty
                    if(board[i][j] == '_'):
                        #Put 'X' in the position
                        board[i][j] = 'X'

                        #New call to the minimax function with the new position
                        #Add one to the depth to know how many moves have been done
                        #isMaximizing is true because it would be the bot's turn
                        eval = self.minimax(board, depth + 1, True)

                        #Undo the move
                        board[i][j] = '_'

                        #Set minEval to the minimum between the current minEval and the eval minimax returned
                        minEval = min(minEval, eval)

            #After all the moves, return the minEval
            return minEval
    
    #Minimax with Alpha-Beta pruning
    def minimaxAB(self, currentBoard, depth, alpha, beta, isMaximizing):
        #Copy the board
        board = [row[:] for row in currentBoard]

        #Evaluate the current position
        result = self.evaluatePosition(board)

        #If someone won or there is a tie
        if result != None:
            #Set eval to the value of the result in the dictionary
            eval = self.scores[result]

            #If is a tie, return 0
            if eval == 0:
                return eval
            
            #If the bot won, return the evaluation minus the depth, we want the fastest way to win
            #If the human won, return the evaluation plus the depth, the human would want the fastest win
            return eval - depth if eval > 0 else eval + depth

        #When is the bot's turn
        if isMaximizing:
            #Set maxEval to a very small value
            maxEval = -math.inf

            #For every possible position in the board
            for i in range(3):
                for j in range(3):
                    #If the box is empty
                    if(board[i][j] == '_'):
                        #Put 'O' in the position
                        board[i][j] = 'O'

                        #New call to the minimax function with the new position
                        #Add one to the depth to know how many moves have been done
                        #isMaximizing is false because it would be the human's turn
                        eval = self.minimaxAB(board, depth + 1, alpha, beta, False)

                        #Undo the move
                        board[i][j] = '_'

                        #Set maxEval to the maximum between the current maxEval and the eval minimax returned
                        maxEval = max(maxEval, eval)
                        #Set alpha to the maximum between the current alpha and the eval minimax returned
                        alpha = max(alpha, eval)
                        #If beta is less or equal to alpha, we dont need to continue trying moves, so we break the loop
                        if beta <= alpha:
                            break

            #After all the moves, return the maxEval
            return maxEval    

        else:
            #Set minEval to a very large value
            minEval = math.inf

            #For every possible position in the board
            for i in range(3):
                for j in range(3):
                    #If the box is empty
                    if(board[i][j] == '_'):
                        #Put 'X' in the position
                        board[i][j] = 'X'

                        #New call to the minimax function with the new position
                        #Add one to the depth to know how many moves have been done
                        #isMaximizing is true because it would be the bot's turn
                        eval = self.minimaxAB(board, depth + 1, alpha, beta, True)

                        #Undo the move
                        board[i][j] = '_'

                        #Set minEval to the minimum between the current minEval and the eval minimax returned
                        minEval = min(minEval, eval)
                        #Set beta to the minimum between the current beta and the eval minimax returned
                        beta = min(beta, eval)
                        #If beta is less or equal to alpha, we dont need to continue trying moves, so we break the loop
                        if beta <= alpha:
                            break

            #After all the moves, return the minEval
            return minEval
    
    #Evaluates if the position has a final result (win or tie)
    def evaluatePosition(self, board):
        for i in range(3):
            if board[i][0] != '_' and board[i][0] == board[i][1] == board[i][2]:
                return board[i][0]
            elif board[0][i] != '_' and board[0][i] == board[1][i] == board[2][i]:
                return board[0][i]

        if board[1][1] != '_' and board[0][0] == board[1][1] == board[2][2]:
            return board[1][1]
        elif board[1][1] != '_' and board[0][2] == board[1][1] == board[2][0]:
            return board[1][1]
        
        for i in board:
            if ('_' in i) == True:
                return None
        
        return 'T'