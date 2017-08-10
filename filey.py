# handles reading to and from puzzle library
import os
import numpy as np

def reader(name):
	dir = os.path.dirname(__file__)
	file_path = os.path.join(dir,'puzzles/')
	file = open(os.path.join(file_path,name),'r+')
	lines = file.readlines()
	
	size = int(lines[0])
	complexity = int(lines[1])
	moves = int(lines[2])
	start = np.loadtxt(lines[4:4+size],dtype='string')
	movelist = []
	for x in range(0,moves):
		movelist.append(np.loadtxt(lines[4+(size+1)*(x+1):4+size+(size+1)*(x+1)],dtype='string'))
	
	file.close()
	return name,size,complexity,moves,start,movelist

def writer(name,size,complexity,moves,start,movelist):
	dir = os.path.dirname(__file__)
	file_path = os.path.join(dir,'puzzles/')
	file = open(os.path.join(file_path,name),'w+')
	
	file.write(str(size)+'\n')
	file.write(str(complexity)+'\n')
	file.write(str(moves)+'\n\n')
	for row in start:
		for item in row:
			file.write(item+' ')
		file.write('\n')
	file.write('\n')
	if movelist:
		for move in movelist:
			for row in move:
				for item in row:
					file.write(item+' ')
				file.write('\n')
			file.write('\n')
	
	file.close()
	return 0
