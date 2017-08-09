# handles reading from puzzle library
import os
import sys
import numpy as np

def reader(puzzle):
	dir = os.path.dirname(__file__)
	file_path = os.path.join(dir,'puzzles/')
	file = open(os.path.join(file_path,puzzle),'r')
	lines = file.readlines()
	
	size = int(lines[0])
	complexity = int(lines[1])
	moves = int(lines[2])
	print size,complexity,moves
	
	start = np.loadtxt(lines[4:4+size],dtype='string')
	movelist = []
	for x in range(0,moves):
		print x
		movelist[x] = np.loadtxt(lines[4+(size+1)*(x+1):4+size+(size+1)*(x+1)],dtype='string')
	print start,'\n'
	for move in movelist:
		print move,'\n'
	
	file.close()
	return 0

def writer():
	dir = os.path.dirname(__file__)
	file_path = os.path.join(dir,'puzzles/')
	file = open(os.path.join(file_path,'test.puz'),'w+')
	
	size = 8
	complexity = 0
	moves = 0
	file.write(str(size)+'\n')
	file.write(str(complexity)+'\n')
	file.write(str(moves)+'\n\n')
	
	file.close()
	return 0
