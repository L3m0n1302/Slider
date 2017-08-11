import phil
import man
import jen


print '----------------------------------------------------------------'

def solver(name,size,complexity,moves,start,solution): # solve and return the optimum move list
	walked = man.walker(start)
	print 'walked in %d moves' % walked[0]
	breath = man.breather(start)
	print 'solved in %d moves' % breath[0]
	solution = []
	path = breath[1][-1][0]
	for i in range(len(path)):
		for move in breath[1]:
			if move[0] == path[:i+1]:
				solution.append(move[1])
				break
	solution.pop(0)
	moves = len(solution)
	return name,size,complexity,moves,start,solution

def main(): # main script body
	
	puz = list(phil.reader('blank.puz'))
	print puz[4]
	puz = solver(*puz)
	print puz[5][-1]
	phil.writer(*puz)
	
	print '----------------------------------------------------------------'
	
	new = ['test.puz',20,0,0,[],[]]
	new[4] = jen.genner(new[1],new[2])
	print new[4]
	new[4] = man.scrambler(new[4])
	print new[4]
	new = solver(*new)
	phil.writer(*new)
	
	return 0

if __name__ == "__main__":
	main()



