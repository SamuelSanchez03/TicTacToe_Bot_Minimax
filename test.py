from bot import Bot
from TTTBoard import TTTBoard

position = [['O', '_', '_'],
            ['O', 'X', 'X'],
            ['_', '_', 'X']]

board = TTTBoard()
board.setBoard(position)

bot = Bot()
move = bot.bestMove(board.getCurrentBoard())

board.update('O', move[0], move[1])
board.printBoard()
print(move)