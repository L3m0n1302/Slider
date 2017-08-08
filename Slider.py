import numpy as np
import random

# matrix block visual labels
block = '+++'
empty = '---'
aim = 'ggg'
finish = '==='

print '----------------------------------------------------------------'

def genner(N,comp): # generates an N*N matrix of complexity comp
		
	# create the starting empty matrix
	start = N*[N*['X'*5]]
	start = np.matrix(start)
	start[:,:] = empty
	
	# create boundary
	start[:,0] = block
	start[:,N-1] = block
	start[0,:] = block
	start[N-1,:] = block
	
	# create the finish point and goal piece
	fin = round(float(N)/2)-1 # finish position on that edge
	start[fin,N-1] = finish # finish point
	start[fin,N-3:N-1] = aim # goal piece
	
	# create extra blocks
	if comp >= 1:
		for _ in xrange(int(round(N/4))):
			bx = random.randint(1,N-2)
			by = random.randint(1,N-2)
			if start[by,bx] == empty:
				if by == fin:
						break
				start[by,bx] = block
	
	# create the rest of the pieces
	counter = int(round(N*0.4))*[0]
	while np.count_nonzero(start == empty) >= (((N-1)**2)*0.25) and counter[0] <=1000:
		legal = False
		while legal == False:
			size = random.randint(2,int(round(N*0.4)))
			bx = random.randint(1,N-2)
			by = random.randint(1,N-2)
			if start[by,bx] != empty:
				counter[0] += 1
				break
			dir = random.choice(['x','y'])
			if dir == 'x':
				if by == fin:
					counter[0] += 1
					break
				if (bx+size <= N-2) and ([start[by,i] for i in range(bx,bx+size)] == size*[empty]):
					counter[size-1] += 1
					start[by,bx:(bx+size)] = '%dx%d' % (size,counter[size-1])
					legal = True
			elif dir == 'y':
				if (by+size <= N-2) and ([start[i,bx] for i in range(by,by+size)] == size*[empty]):
					counter[size-1] += 1
					start[by:(by+size),bx] = '%dy%d' % (size,counter[size-1])
					legal = True
	
	start = scrambler(start)
	if checker(start) == True:
		start = genner(N,comp)
	return start

def scrambler(state):
	counter = 0
	while True:
		moves = mover(state)
		state = random.choice(moves)
		counter += 1
		if counter == 1000:
			return state

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

def solver(state,size,complexity):
	if type(state) == int:
		state = genner(size,complexity)
	print state
	print 'walking...'
	walked = walker(state)
	print 'walked in %d moves' % walked[0]
	print 'solving...'
	breath = breather(state)
	print 'solved in %d moves' % breath[0]
	print breath[1][-1][1]

def setter(): # make a preset matrix / moves = 18
	mat = 8*[8*[block*5]]
	mat = np.matrix(mat)
	mat[:,:] = empty
	
	mat[:,0] = block
	mat[:,7] = block
	mat[0,:] = block
	mat[7,:] = block
	
	mat[3,7] = finish
	
	mat[3,2:4] = '%sx' % aim
	
	mat[4,1:3] = '2x1'
	mat[4,3:5] = '2x2'
	
	mat[6,4:7] = '3x1'
	
	mat[2:4,1] = '2y1'
	mat[5:7,1] = '2y2'
	mat[5:7,2] = '2y3'
	mat[5:7,3] = '2y4'
	mat[2:4,4] = '2y5'
	mat[2:4,6] = '2y6'
	mat[4:6,6] = '2y7'
	
	mat[2:5,5] = '3y1'
	
	return mat

def main(): # main script body
	
	set = setter()
	# solver(set,0,0)
	solver(0,8,0)
	
	
	return 0

if __name__ == "__main__":
	main()



