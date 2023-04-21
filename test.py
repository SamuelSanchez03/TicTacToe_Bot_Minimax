from bot import Bot
from TTTBoard import TTTBoard
import time

position = [['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', 'X']]

board = TTTBoard()
board.setBoard(position)

bot = Bot()
startTime = time.time()
move = bot.bestMove(board.getCurrentBoard())
lapTime = time.time()
print(move)
print("Time without alpha-beta =", lapTime - startTime)

move = bot.bestMoveAB(board.getCurrentBoard())
print(move)
print("Time with alpha-beta =", time.time() - lapTime) 

#board.update('O', move[0], move[1])
#board.printBoard()