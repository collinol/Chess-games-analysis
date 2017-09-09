from pylab import *
import numpy as np
import os


fname = "chess_com_games_page*"
game_records = []
cats = ['Event ', 'Site ','Date ','Round ','White ','Black ','Result ','WhiteElo ','BlackElo ','TimeControl ','EndTime ','Termination '
]

for fname in os.listdir('.'):    # change directory as needed
    if os.path.isfile(fname):    # make sure it's a file, not a directory entry
        with open(fname) as f:   # open file
            for line in f:       # process line by line

               	line = line.split('\n')[0].strip('[').strip(']').split('"')[0:2]
		if line[0] == 'Event ':
			single_game = []
			moves = []
		if line[0] == 'Date ' or line[0] == 'White ' or line[0] == 'Black ' or line[0] == 'Termination ':
			single_game.append((line[0],line[1]))
		if line[0] not in cats:
			moves.append(line[0])

		if line[0] == '':
			if len(moves) != 1:
				single_game.append(('moves',moves))
		if len(single_game) == 5: 
			game_records.append(single_game)



column_reference = "a b c d e f g h".split(" ")
EMPTY_SQUARE = " "
 
class Model(object):
    def __init__(self):
        '''create a chess board with pieces positioned for a new game
        row ordering is reversed from normal chess representations
        but corresponds to a top left screen coordinate 
        '''
         
        self.board = []
        pawn_base = "a2 b2 c2 d2 e2 f2 g2 h2"
        white_pieces =  "a1 b1 c1 d1 e1 f1 g1 h1"
        white_pawns = pawn_base.strip() 
        black_pieces = "a8 b8 c8 d8 e8 f8 g8 h8"
        black_pawns = "a7 b7 c7 d7 e7 f7 g7 h7"
	sixth_rank ="a6 b6 c6 d6 e6 f6 g6 h6"
	fifth_rank = "a5 b5 c5 d5 e5 f5 g5 h5"
	fourth_rank = "a4 b4 c4 d4 e4 f4 g4 h4"
	third_rank = "a3 b3 c3 d3 e3 f3 g3 h3"	
        self.board.append(black_pieces.split(" "))
        self.board.append(black_pawns.split(" "))
        self.board.append(sixth_rank.split(" "))
	self.board.append(fifth_rank.split(" "))
	self.board.append(fourth_rank.split(" "))
	self.board.append(third_rank.split(" "))
        self.board.append(white_pawns.split(" "))
        self.board.append(white_pieces.split(" "))
 

class View(object):
    def __init__(self):
	pass
    def display(self,  board):
	print("%s: %s"%(" ", column_reference))
	print("-"*50)
	for i, row in enumerate(board):
	    row_marker = 8-i
	    print("%s: %s"%(row_marker,  row))

#points
Points_pieces ={('a',1),('b',1),('c',1),('d',1),('e',1),('f',1),('g',1),('h',1),('B',3),('N',3),('Q',9),('R',5),('K',0)}
Points_pieces = dict(Points_pieces)

Points_board = {}
letters = "a b c d e f g h"
letters = letters.split(" ")
nums = "1 2 3 4 5 6 7 8"
nums = nums.split(" ")
for l in letters:
	for n in nums:
		if n == '7' or n == '2':
			Points_board[l+n] = 1
		if n == '8' or n == '1':
			if l == 'a' or l == 'h':
				Points_board[l+n] = 5
			if l == 'b' or l == 'g':
				Points_board[l+n] = 3
			if l == 'c' or l == 'f':
				Points_board[l+n] = 3
			if l == 'd':
				Points_board[l+n] = 9
			if l == 'e':
				Points_board[l+n] = 0
		else: Points_board[l+n] = 0


m = Model()
board = np.array(m.board)


for i in game_records:
	
	wpoints = 0
	bpoints = 0
	date = i[0]
	datenum = date[1].split('.')
	datenum = int(datenum[1])*1000000+int(datenum[2])*10000+int(datenum[0])
	white = i[1]
	black = i[2]
	result = i[3]
	moves = i[4]
	complete_moves = []
	for j in moves[1][1:-1]:
		for m in j.split(' '):
			complete_moves.append(m)
	
	moves = complete_moves[0:-1]

	Moves = {}

	for m,pair in enumerate(moves):
		if '.' in pair:
			try:Moves[int(pair.strip('.'))] = ((moves[m+1],moves[m+2]))
			except:continue
	

	for k in sorted(Moves.keys()):
		#NEED TO DEAL WITH PAWN=Q+ EXCEPTIONS!!
		w = Moves[k][0]
		b = Moves[k][1]
		#excluding castling
		if '+' in w: w = w.strip('+')
		if '#' in w: w = w.strip('#')
		if '+' in b: b = b.strip('+')
		if '#' in b: b = b.strip('#')
		if w[0] != 'O':
			#moves without capture
			if 'x' not in w:
				if w[0].isupper():			
					Points_board[w[1:2]] = Points_pieces[w[0]]
				else:	Points_board[w] = 1
			else:
				#replacement
				#get current points on square
				#add to white's total
				#replace with new points
				wpoints += int(Points_board[w.split('x')[1]])
				Points_board[w.split('x')[1]] = Points_pieces[w[0]]
		if b[0] != 'O':
			#moves without capture
			if 'x' not in b:
				if b[0].isupper():				
					Points_board[b[1:2]] = Points_pieces[b[0]]
				else:	Points_board[b] = 1
					
			else:
				#replacement
				#get current points on square
				#add to black's total
				#replace bith new points
				bpoints += int(Points_board[b.split('x')[1]])
				Points_board[b.split('x')[1]] = Points_pieces[b[0]]
	
		#castle cases
		if w == 'O-O':
			Points_board['b1'] = 0
			Points_board['c1'] = 5
		if w == 'O-O-O':
			Points_board['f1'] = 0
			Points_board['e1'] =5
		if b == 'O-O':
			Points_board['b8'] = 0
			Points_board['c8'] = 5
		if b == 'O-O-O':
			Points_board['f8'] = 0
			Points_board['e8'] =5

	#calculate total - gonna be different for worldwide (me not involved), not sure how though
	

	

	if white[1] == 'GetSchwifty10':
		my_net = wpoints-bpoints
	if black[1] == 'GetSchwifty10':
		my_net = bpoints-wpoints

	sys.stdout.write("{:<25}{:<42}{:<15}\n".format('Date: '+date[1], result[1],'Final Point Difference '+str(my_net)))	
	
	#left off ^^ - now collect and graph















