# block puzzle solver and generator

import phil
import man
import jen

def solver(name, size, complexity, moves, start, solution): # solve and return the optimum move list
    walked = man.walker(start)
    print('walked in {0} moves'.format(walked[0]))
    breath = man.breather(start)
    print('solved in {0} moves'.format(breath[0]))
    solution = []
    path = breath[1][-1][0]
    for i in range(len(path)):
        for move in breath[1]:
            if move[0] == path[:i+1]:
                solution.append(move[1])
                break
    solution.pop(0)
    moves = len(solution)
    return name, size, complexity, moves, start, solution

def main(): # main script body

    print('----------------------------------------------------------------')

    puz = list(phil.reader('blank.puz'))
    puz = solver(*puz)
    print(puz[4])
    print(puz[5][-1])
    phil.writer(*puz)

    print('----------------------------------------------------------------')

    test = ['test.puz', 8, 0, 0, [], []]
    test[4] = jen.genner(test[1], test[2])
    test[4] = man.scrambler(test[4])
    print(test[4])
    test = solver(*test)
    print(test[5][-1])
    phil.writer(*test)

    return 0

if __name__ == "__main__":
    main()
