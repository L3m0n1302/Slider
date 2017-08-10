import filey
import jenny
import manny

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
	if manny.checker(start) == True:
		start = genner(N,comp)
	return start

def scrambler(state):
	counter = 0
	while True:
		moves = manny.mover(state)
		state = random.choice(moves)
		counter += 1
		if counter == 1000:
			return state

def solver(state): # solve and return the optimum move list
	print 'walking...'
	walked = manny.walker(state)
	print 'walked in %d moves' % walked[0]
	print 'solving...'
	breath = manny.breather(state)
	print 'solved in %d moves' % breath[0]
	print breath[1][-1][1]
	

def main(): # main script body
	
	puz1 = filey.reader('puzzle1.puz')
	print puz1[0:5]
	solver(puz1[4])
	
	filey.writer(*puz1)
	
	
	# solver(puz1)
	# solver(0,8,0)
	
	# new = genner(size,complexity)
	
	return 0

if __name__ == "__main__":
	main()



