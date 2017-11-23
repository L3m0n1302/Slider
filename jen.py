"""handles puzzle generation"""

import random
import itertools
import math
import numpy as np

block = '+++'
empty = '---'
aim = '***'
finish = '==='

def genner(N, comp):
    """generate an NxN matrix of complexity comp"""
    # create the starting basic matrix
    #start = np.empty((N, N), dtype='U3')
    start = np.chararray((N, N), itemsize=3, unicode=True)
    start[:, :] = empty
    start[:, 0] = block
    start[:, N-1] = block
    start[0, :] = block
    start[N-1, :] = block
    fin = N//2-1 # finish position on that edge
    start[fin, N-1] = finish # finish point
    start[fin, N-3:N-1] = aim # goal piece
    # create extra blocks
    if comp >= 1:
        for _ in itertools.repeat(None, N//4):
            bx = random.randint(1, N-2)
            by = random.randint(1, N-2)
            if start[by, bx] == empty:
                if by == fin:
                    break
                start[by, bx] = block
    # create the rest of the pieces
    counter = math.ceil(N*0.4)*[0]
    xy = itertools.cycle(['x', 'y'])
    while np.count_nonzero(start == empty) >= (((N-1)**2)*0.25) and counter[0] <= 100:
        legal = False
        while not legal:
            size = random.randint(2, math.ceil(N*0.4))
            bx = random.randint(1, N-2)
            by = random.randint(1, N-2)
            if start[by, bx] != empty:
                counter[0] += 1
                break
            direc = next(xy)
            if direc == 'x':
                if by == fin:
                    counter[0] += 1
                    break
                if (bx+size <= N-2) and ([start[by, i] for i in range(bx, bx+size)] == size*[empty]):
                    counter[size-1] += 1
                    start[by, bx:(bx+size)] = '%dx%d' % (size, counter[size-1])
                    legal = True
            elif direc == 'y':
                if (by+size <= N-2) and ([start[i, bx] for i in range(by, by+size)] == size*[empty]):
                    counter[size-1] += 1
                    start[by:(by+size), bx] = '%dy%d' % (size, counter[size-1])
                    legal = True
    return start
