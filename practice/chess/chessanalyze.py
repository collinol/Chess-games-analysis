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

#points
Points ={('a',1),('b',1),('c',1),('d',1),('e',1),('f',1),('g',1),('h',1),('B',3),('N',3),('Q',9),
('R',5),('K',1000)}

for i in game_records:
	
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
			except: continue

EMPTY_SQUARE = " "
 
class Model(object):
    def __init__(self):
        '''create a chess board with pieces positioned for a new game
        row ordering is reversed from normal chess representations
        but corresponds to a top left screen coordinate 
        '''
         
        self.board = []
        pawn_base = "P "*8
        white_pieces =  "R N B Q K B N R"
        white_pawns = pawn_base.strip() 
        black_pieces = white_pieces.lower()
        black_pawns = white_pawns.lower()
        self.board.append(black_pieces.split(" "))
        self.board.append(black_pawns.split(" "))
        for i in range(4):
            self.board.append([EMPTY_SQUARE]*8)
        self.board.append(white_pawns.split(" "))
        self.board.append(white_pieces.split(" "))

column_reference = "a b c d e f g h".split(" ")
class View(object):
    def __init__(self):
        pass
    def display(self,  board):
        print("%s: %s"%(" ", column_reference))
        print("-"*50)
        for i, row in enumerate(board):
            row_marker = 8-i
            print("%s: %s"%(row_marker,  row))
m = Model()
v = View()
v.display(m.board)
	
		























