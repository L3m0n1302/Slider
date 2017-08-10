# manipulate a given game state in various ways

import random

block = '+++'
empty = '---'
aim = 'ggg'
finish = '==='

def director(state,posy,posx,direction): # figure if a move is possible from a spot in each direction
	i = 0
	if direction == 'up':
		while state[posy+i,posx] == empty:
			i +=1
		if 'y' in state[posy+i,posx]:
			return 'True',i,state[posy+i,posx]
	elif direction == 'down':
		while state[posy-i,posx] == empty:
			i +=1
		if 'y' in state[posy-i,posx]:
			return 'True',i,state[posy-i,posx]
	elif direction == 'left':
		while state[posy,posx+i] == empty:
			i +=1
		if ('x' in state[posy,posx+i]) or (state[posy,posx+i] == aim):
			return 'True',i,state[posy,posx+i]
	elif direction == 'right':
		while state[posy,posx-i] == empty:
			i +=1
		if ('x' in state[posy,posx-i]) or (state[posy,posx-i] == aim):
			return 'True',i,state[posy,posx-i]
	return 0,0,0

def mover(state): # given a game state find all possible movements
	movelist = [] # list of possible moves
	moveset = [] # list of states resulting from possible moves
	for y in range(1,len(state)-1):
		for x in range(1,len(state)-1):
			if state[y,x] == empty:
				for direction in ['up','down','left','right']:
					tf,i,value = director(state,y,x,direction)
					if tf == 'True':
						movelist.append([y,x,i,direction,value])
	for move in movelist:
		tempstate = state.copy()
		length = move[4][0]
		if length in aim:
			length = 2
		length = int(length)
		if move[3] == 'up':
			tempstate[move[0]+move[2]:move[0]+move[2]+length,move[1]] = empty
			tempstate[move[0]:move[0]+length,move[1]] = move[4]
		elif move[3] == 'down':
			tempstate[move[0]-move[2]-length+1:move[0]-move[2]+1,move[1]] = empty
			tempstate[move[0]-length+1:move[0]+1,move[1]] = move[4]
		elif move[3] == 'left':
			tempstate[move[0],move[1]+move[2]:move[1]+move[2]+length] = empty
			tempstate[move[0],move[1]:move[1]+length] = move[4]
		elif move[3] == 'right':
			tempstate[move[0],move[1]-move[2]-length+1:move[1]-move[2]+1] = empty
			tempstate[move[0],move[1]-length+1:move[1]+1] = move[4]
		moveset.append(tempstate)
	return moveset
	
def checker(state): # check if the current state is solved
	N = len(state)
	if state[round(float(N)/2)-1,N-2] == aim:
		return 1
	else:
		return 0

def walker(start): # random walk to see if a solution is possible
	road = [start]
	while True:
		fork = mover(road[-1])
		state = random.choice(fork)
		road.append(state)
		if checker(state) == 1:
			return len(road)-1,road

def breather(start): # breadth first search / fInd all possible moves until solved
	tree = [[[0],start]] # decision tree of moves
	queue = [[[0],start]] # queue of states to explore
	seen = [start] # seen states
	while True:
		newqueue = []
		for state in queue:
			branch = mover(state[1])
			for move in seen: # check for dead end
				for i in range(len(branch)):
					if (move == branch[i]).all():
						del branch[i]
						break
			seen.extend(branch)
			for j in range(len(branch)):
				label = state[0][:]
				label.append(j)
				newqueue.append([label,branch[j]])
				if checker(branch[j]) == 1: # check if solved
					tree.extend(newqueue)
					return len(label)-1,tree
		tree.extend(newqueue)
		queue = newqueue[:]
		if not queue:
			return 0,tree
		print '(%d,%d)' % (len(queue),len(tree))
	
	



