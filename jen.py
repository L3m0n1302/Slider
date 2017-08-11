# handles puzzle generation
import random
import numpy as np
import itertools

block = '+++'
empty = '---'
aim = 'ggg'
finish = '==='

def genner(N,comp): # generates an NxN matrix of complexity comp
		
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
	xy = itertools.cycle(['x','y'])
	while np.count_nonzero(start == empty) >= (((N-1)**2)*0.25) and counter[0] <=100:
		legal = False
		while legal == False:
			size = random.randint(2,int(round(N*0.4)))
			bx = random.randint(1,N-2)
			by = random.randint(1,N-2)
			if start[by,bx] != empty:
				counter[0] += 1
				break
			dir = next(xy)
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
	return start



