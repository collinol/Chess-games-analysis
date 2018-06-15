from numpy import *
import pylab as pl
import matplotlib.pyplot as plt
white_pawns = open('White_Pawn_Moves.txt','r')
white_nights = open('White_Knight_Moves.txt','r')
white_bishops = open('White_Bishop_Moves.txt','r')
white_rooks = open('White_Rook_Moves.txt','r')
white_queen = open('White_Queen_Moves.txt','r')
white_king  = open('White_King_Moves.txt','r')
black_pawns = open('Black_Pawn_Moves.txt','r')
black_nights = open('Black_Knight_Moves.txt','r')
black_bishops = open('Black_Bishop_Moves.txt','r')
black_rooks = open('Black_Rook_Moves.txt','r')
black_queen = open('Black_Queen_Moves.txt','r')
black_king = open('Black_King_Moves.txt','r')


letters = "a b c d e f g h"
letters = letters.split(" ")
nums = "8 7 6 5 4 3 2 1"
nums = nums.split(" ")


Board = {}
for i in range(8):
	for j in range(8):
		position = letters[j]+nums[i]
		Board[position] = ((i,j))

def matrix_freq(piece_file):
	piece_file.seek(0)
	board = zeros((8,8))
	for line in piece_file:
		line = line.split('\n')[0]
		try:board[Board[line.split(' ')[0]][0],Board[line.split(' ')[0]][1]] = line.split(' ')[1]
		except:pass
	#print board
	boardmax,boardmin = board.max(), board.min()
	board = (board-boardmin) / (boardmax - boardmin)
	rotated = flipud(board)
	#print rotated
	return rotated
#matrix_freq(white_king)
#quit()
all_pieces = [white_pawns,white_nights,white_bishops,white_rooks,white_queen,white_king,black_pawns,black_nights,black_bishops,black_rooks,black_queen,black_king]


str_pieces = ['White Pawns','White Knights','White Bishops','White Rooks','White Queen','White King','Black Pawns','Black Knights','Black Bishops','Black Rooks','Black Queen' ,'Black King']

import matplotlib.ticker as ticker

fig,axes = plt.subplots(nrows = 3, ncols = 2)


c = matrix_freq(white_pawns)
plt.subplot(4,4,1,aspect ='equal')
cbar = plt.pcolor(c, edgecolors='k', linestyle= 'solid', linewidths=0.2, cmap='gist_gray')
xticksloc = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]
xtickslbl = ['a','b','c','d','e','f','g','h']
pl.gca().set_xticklabels(xtickslbl)
pl.gca().set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
pl.gca().set_yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
ytickslbl = ['1','2','3','4','5','6','7','8']
pl.gca().set_yticklabels(ytickslbl)
plt.colorbar(cbar)
plt.title("White Pawns")

plt.subplot(4,4,2,aspect ='equal')
c = matrix_freq(black_pawns)
cbar = plt.pcolor(c, edgecolors='k', linestyle= 'solid', linewidths=0.2, cmap='binary')
xticksloc = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]
xtickslbl = ['a','b','c','d','e','f','g','h']
pl.gca().set_xticklabels(xtickslbl)
pl.gca().set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
pl.gca().set_yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
ytickslbl = ['1','2','3','4','5','6','7','8']
pl.gca().set_yticklabels(ytickslbl)
plt.colorbar(cbar)
plt.title("Black Pawns")

plt.subplot(4,4,3,aspect ='equal')
c = matrix_freq(white_nights)
cbar = plt.pcolor(c, edgecolors='k', linestyle= 'solid', linewidths=0.2, cmap='gist_gray')
xticksloc = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]
xtickslbl = ['a','b','c','d','e','f','g','h']
pl.gca().set_xticklabels(xtickslbl)
pl.gca().set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
pl.gca().set_yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
ytickslbl = ['1','2','3','4','5','6','7','8']
pl.gca().set_yticklabels(ytickslbl)
plt.colorbar(cbar)
plt.title("White Knights")


plt.subplot(4,4,4,aspect ='equal')
c = matrix_freq(black_nights)
cbar = plt.pcolor(c, edgecolors='k', linestyle= 'solid', linewidths=0.2, cmap='binary')
xticksloc = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]
xtickslbl = ['a','b','c','d','e','f','g','h']
pl.gca().set_xticklabels(xtickslbl)
pl.gca().set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
pl.gca().set_yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
ytickslbl = ['1','2','3','4','5','6','7','8']
pl.gca().set_yticklabels(ytickslbl)
plt.colorbar(cbar)
plt.title("Black Knights")

plt.subplot(4,4,5,aspect ='equal')
c = matrix_freq(white_bishops)
cbar = plt.pcolor(c, edgecolors='k', linestyle= 'solid', linewidths=0.2, cmap='gist_gray')
xticksloc = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]
xtickslbl = ['a','b','c','d','e','f','g','h']
pl.gca().set_xticklabels(xtickslbl)
pl.gca().set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
pl.gca().set_yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
ytickslbl = ['1','2','3','4','5','6','7','8']
pl.gca().set_yticklabels(ytickslbl)
plt.colorbar(cbar)
plt.title("White Bishops")

plt.subplot(4,4,6,aspect ='equal')
c = matrix_freq(black_bishops)
cbar = plt.pcolor(c, edgecolors='k', linestyle= 'solid', linewidths=0.2, cmap='binary')
xticksloc = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]
xtickslbl = ['a','b','c','d','e','f','g','h']
pl.gca().set_xticklabels(xtickslbl)
pl.gca().set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
pl.gca().set_yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
ytickslbl = ['1','2','3','4','5','6','7','8']
pl.gca().set_yticklabels(ytickslbl)
plt.colorbar(cbar)
plt.title("Black Bishops")

plt.subplot(4,4,7,aspect ='equal')
c = matrix_freq(white_rooks)
cbar = plt.pcolor(c, edgecolors='k', linestyle= 'solid', linewidths=0.2, cmap='gist_gray')
xticksloc = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]
xtickslbl = ['a','b','c','d','e','f','g','h']
pl.gca().set_xticklabels(xtickslbl)
pl.gca().set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
pl.gca().set_yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
ytickslbl = ['1','2','3','4','5','6','7','8']
pl.gca().set_yticklabels(ytickslbl)
plt.colorbar(cbar)
plt.title("White Rooks")

plt.subplot(4,4,8,aspect ='equal')
c = matrix_freq(black_rooks)
cbar = plt.pcolor(c, edgecolors='k', linestyle= 'solid', linewidths=0.2, cmap='binary')
xticksloc = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]
xtickslbl = ['a','b','c','d','e','f','g','h']
pl.gca().set_xticklabels(xtickslbl)
pl.gca().set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
pl.gca().set_yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
ytickslbl = ['1','2','3','4','5','6','7','8']
pl.gca().set_yticklabels(ytickslbl)
plt.colorbar(cbar)
plt.title("Black Rooks")

plt.subplot(4,4,9,aspect ='equal')
c = matrix_freq(white_queen)
cbar = plt.pcolor(c, edgecolors='k', linestyle= 'solid', linewidths=0.2, cmap='gist_gray')
xticksloc = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]
xtickslbl = ['a','b','c','d','e','f','g','h']
pl.gca().set_xticklabels(xtickslbl)
pl.gca().set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
pl.gca().set_yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
ytickslbl = ['1','2','3','4','5','6','7','8']
pl.gca().set_yticklabels(ytickslbl)
ytickslbl = ['1','2','3','4','5','6','7','8']
pl.gca().set_yticklabels(ytickslbl)
plt.colorbar(cbar)
plt.title("White Queen")

plt.subplot(4,4,10,aspect ='equal')
c = matrix_freq(black_queen)
cbar = plt.pcolor(c, edgecolors='k', linestyle= 'solid', linewidths=0.2, cmap='binary')
xticksloc = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]
xtickslbl = ['a','b','c','d','e','f','g','h']
pl.gca().set_xticklabels(xtickslbl)
pl.gca().set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
pl.gca().set_yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
ytickslbl = ['1','2','3','4','5','6','7','8']
pl.gca().set_yticklabels(ytickslbl)
plt.colorbar(cbar)
plt.title("Black Queen")

plt.subplot(4,4,11,aspect ='equal')
c = matrix_freq(white_king)
cbar = plt.pcolor(c, edgecolors='k', linestyle= 'solid', linewidths=0.2, cmap='gist_gray')
xticksloc = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]
xtickslbl = ['a','b','c','d','e','f','g','h']
pl.gca().set_xticklabels(xtickslbl)
pl.gca().set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
pl.gca().set_yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
ytickslbl = ['1','2','3','4','5','6','7','8']
pl.gca().set_yticklabels(ytickslbl)
plt.colorbar(cbar)
plt.title("White King")

plt.subplot(4,4,12,aspect ='equal')
c = matrix_freq(black_king)
cbar = plt.pcolor(c, edgecolors='k', linestyle= 'solid', linewidths=0.2, cmap='binary')
xticksloc = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]
xtickslbl = ['a','b','c','d','e','f','g','h']
pl.gca().set_xticklabels(xtickslbl)
pl.gca().set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
pl.gca().set_yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
ytickslbl = ['1','2','3','4','5','6','7','8']
pl.gca().set_yticklabels(ytickslbl)
plt.colorbar(cbar)
plt.title("Black King")

plt.suptitle("Most Frequently Moved-To Positions of Each Chess Piece")
plt.show()






