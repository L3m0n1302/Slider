"""handles file reading to and from puzzle library"""

import os
import numpy as np

def reader(name):
    """reads a puzzle and its attributes from a file"""
    direc = os.path.dirname(__file__)
    file_path = os.path.join(direc, 'puzzles', name)
    file = open(file_path, 'r+')
    lines = file.readlines()
    size = int(lines[0])
    complexity = int(lines[1])
    moves = int(lines[2])
    start = np.chararray((size, size), itemsize=3, unicode=True)
    for i in range(0, size):
        start[i, :] = lines[4+i].split()
    solution = []
    for x in range(0, moves):
        move = np.chararray((size, size), itemsize=3, unicode=True)
        for i in range(0, size):
            move[i, :] = lines[4+i+(size+1)*(x+1)].split()
        solution.append(move)
    file.close()
    return name, size, complexity, moves, start, solution

def writer(name, size, complexity, moves, start, solution):
    """writes a puzzle and its attributes to a file"""
    direc = os.path.dirname(__file__)
    file_path = os.path.join(direc, 'puzzles/')
    file = open(os.path.join(file_path, name), 'w+')
    file.write(str(size)+'\n')
    file.write(str(complexity)+'\n')
    file.write(str(moves)+'\n\n')
    for y in range(len(start)):
        for x in range(len(start)):
            file.write(start[y, x]+' ')
        file.write('\n')
    file.write('\n')
    if solution:
        for move in solution:
            for y in range(len(move)):
                for x in range(len(move)):
                    file.write(move[y, x]+' ')
                file.write('\n')
            file.write('\n')
    file.close()
    return 0
