from bot import Bot
from TTTBoard import TTTBoard
import time

position = [['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', 'X']]

board = TTTBoard()
board.setBoard(position)

bot = Bot()

#'''
startTime = time.time()
move = bot.bestMove(board.getCurrentBoard())
lapTime = time.time()
print("Time without alpha-beta =", round((lapTime - startTime)*1000, 2), "miliseconds")
print("Best move:", move)

move = bot.bestMoveAB(board.getCurrentBoard())
print("Time with alpha-beta =", round((time.time() - lapTime)*1000, 2), "miliseconds")
print("Best move:", move)

'''
position = [['O', '_', '_'],
            ['O', 'X', 'X'],
            ['_', '_', 'X']]

board.setBoard(position)
move = bot.bestMoveAB(board.getCurrentBoard())
print("Best move:", move)
board.update('O', move[0], move[1])
board.printBoard()
'''