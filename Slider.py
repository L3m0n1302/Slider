"""block puzzle solver and generator"""

import phil
import man

def solver(name, size, complexity, moves, start, solution):
    """solve and return the optimum move list"""
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

def main():
    """main script body"""
    print('----------------------------------------------------------------')
    test1 = list(phil.reader('blank.puz'))
    print(test1[4])
    test1 = solver(*test1)
    print(test1[5][-1])
    phil.writer(*test1)
    print('----------------------------------------------------------------')
    test2 = ['test.puz', 8, 0, 0, [], []]
    test2[4] = man.genner(test2[1], test2[2])
    print(test2[4])
    test2[4] = man.scrambler(test2[4])
    print(test2[4])
    test2 = solver(*test2)
    print(test2[5][-1])
    phil.writer(*test2)
    print('----------------------------------------------------------------')
    return 0

if __name__ == "__main__":
    main()
