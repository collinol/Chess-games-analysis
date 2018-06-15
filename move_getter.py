from pylab import *
import numpy as np
import os


f = open("WorldGames_bigger_sample.pgn",'r')
cats = ['Event ', 'Site ','Date ','Round ','White ','Black ','Result ','WhiteElo ','BlackElo ','TimeControl ','EndTime ','Termination ', 'ECO ',''
]
move_count = 0
WP = {}
WN = {}
WB = {}
WR = {}
WQ = {}
WK = {}

BP = {}
BN = {}
BB = {}
BR = {}
BQ = {}
BK = {}


def NonCastleMove(move,Dict):
	if 'x' not in move:
		if move[0].isupper():
			if len(move[1:])>2:
				if move[2:] not in Dict:
					Dict[move[2:]] = 1
				if move[2:] in Dict:
					Dict[move[2:]] += 1
			else:
				if move[1:] not in Dict:
					Dict[move[1:]] = 1
				if move[1:] in Dict:
					Dict[move[1:]] += 1
	if 'x' in move:
		move = move.split('x')
		if move[0].isupper():
			if len(move[1])>2:
				if move[1][2:] not in Dict:
					Dict[move[1][2:]] = 1
				if move[1][2:] in Dict:
					Dict[move[1][2:]] += 1
			else:
				if move[1] not in Dict:
					Dict[move[1]] = 1
				if move[1] in Dict:
					Dict[move[1]] += 1
	return Dict

events = 0
for line in f:  
	line = line.split('\n')[0].strip('[').strip(']').split('"')[0:2]
	
	if line[0] == 'Event ': events += 1
	if line[0] not in cats:
		
		for i in line[0].split(' '):

			if i== '1-0' or i == '1/2-1/2' or i == '0-1' :
				move_count = 0
			if i != '' and i!= '1-0' and i!= '1/2-1/2' and i != '0-1' and '.' not in i:
				#handle move dictionaries in here instead of for looping again
				if move_count%2 == 0: 
					w = i
					if '+' in w: w = w.strip('+')
					if '#' in w: w = w.strip('#')
					if '=' in w: w = w.strip('=')
					#non castle moves
					if 'O' not in w:

						if w[0] == 'K':
							NonCastleMove(w,WK)
						if w[0] == 'B':
							NonCastleMove(w,WB)
						if w[0] == 'N':
							NonCastleMove(w,WN)
						if w[0] == 'Q':
							NonCastleMove(w,WQ)
						if w[0] == 'R':
							NonCastleMove(w,WR)

						if w[0].isupper() == False:
							if '=' in w: w = w.split('=')[0]
							if 'x' not in w:
								if w not in WP:
									WP[w] = 1
								if w in WP: WP[w] += 1
							if 'x' in w:
								w = w.split('x')
								if w[1] not in WP:
									WP[w[1]] = 1
								if w[1] in WP: WP[w[1]] += 1
					#Castles
					if w == 'O-O':
						if 'g1' not in WK.keys():
							WK['g1'] = 1
						if 'g1' in WK.keys():
							WK['g1'] += 1
						if 'f1' not in WR.keys():
							WR['f1'] = 1
						if 'f1' in WR.keys():
							WR['f1'] += 1
					if w == 'O-O-O':
						if 'c1' not in WK.keys():
							WK['c1'] = 1
						if 'c1' in WK.keys():
							WK['c1'] += 1
						if 'd1' not in WR.keys():
							WR['d1'] = 1
						if 'd1' in WR.keys():
							WR['d1'] += 1
					
						
						
			


				if move_count%2 != 0: 
					b = i
					if '+' in b: b = b.strip('+')
					if '#' in b: b = b.strip('#')
					if '=' in b: b = b.strip('=')
					#non castle moves
					if 'O' not in b:

						if b[0] == 'K':
							NonCastleMove(b,BK)
						if b[0] == 'B':
							NonCastleMove(b,BB)
						if b[0] == 'N':
							NonCastleMove(b,BN)
						if b[0] == 'Q':
							NonCastleMove(b,BQ)
						if b[0] == 'R':
							NonCastleMove(b,BR)

						if b[0].isupper() == False:
							if '=' in b: b = b.split('=')[0]
							if 'x' not in b:
								if b not in BP:
									BP[b] = 1
								if b in BP: BP[b] += 1
							if 'x' in b:
								b = b.split('x')
								if b[1] not in BP:
									BP[b[1]] = 1
								if b[1] in BP: BP[b[1]] += 1
					#Castles
					if b == 'O-O':
						if 'g8' not in BK.keys():
							BK['g8'] = 1
						if 'g8' in BK.keys():
							BK['g8'] += 1
						if 'f8' not in BR.keys():
							BR['f8'] = 1
						if 'f8' in BR.keys():
							BR['f8'] += 1
					if b == 'O-O-O':
						if 'c8' not in BK.keys():
							BK['c8'] = 1
						if 'c8' in BK.keys():
							BK['c8'] += 1
						if 'd8' not in BR.keys():
							BR['d8'] = 1
						if 'd8' in BR.keys():
							BR['d8'] += 1
					#handle move dictionaries in here instead of for looping again
		
				move_count+=1

print events ,' games analyzed'

def FileWriter(filename, dictionary):
	myfile = open(filename, 'w')
	for k,v in dictionary.iteritems():
		line = k+' '+str(v)+'\n'
		myfile.write(line)

	myfile.close()
FileWriter('White_Pawn_Moves.txt',WP)
FileWriter('White_Knight_Moves.txt',WN)
FileWriter('White_Bishop_Moves.txt',WB)
FileWriter('White_Rook_Moves.txt',WR)
FileWriter('White_Queen_Moves.txt',WQ)
FileWriter('White_King_Moves.txt',WK)
FileWriter('Black_Pawn_Moves.txt',BP)
FileWriter('Black_Knight_Moves.txt',BN)
FileWriter('Black_Bishop_Moves.txt',BB)
FileWriter('Black_Rook_Moves.txt',BR)
FileWriter('Black_Queen_Moves.txt',BQ)
FileWriter('Black_King_Moves.txt',BK)

print 'files written - format: (White/black)_(Piece)_Moves.txt'








