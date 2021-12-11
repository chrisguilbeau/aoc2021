from sys import argv
from collections import Counter
from itertools import chain

class Board:
    def __init__(self, lines):
        n2c = {}
        for i, line in enumerate(lines):
            for j, num in enumerate(line.split()):
                n2c[num] = (i, j)
        self.n2c = n2c
        self.c2n = {v: k for k, v in self.n2c.items()}
        self.coords = []
        self.nums = []
        self.won = False
    def pick(self, num):
        if not self.won:
            coord = self.n2c.get(num)
            if coord:
                self.coords.append(coord)
                self.nums.append(num)
    def check(self):
        if not self.won:
            for column, count in chain(
                    Counter(i for i, _ in self.coords).items(),
                    Counter(i for _, i in self.coords).items()
                    ):
                if count == 5:
                    print('winner!')
                    lastPicked = int(self.nums[-1])
                    unpickedNums = []
                    for n in self.n2c:
                        if n not in self.nums:
                            unpickedNums.append(int(n))
                    print(lastPicked)
                    print(unpickedNums)
                    print(sum(unpickedNums))
                    print(lastPicked * sum(unpickedNums))
                    self.won = True
                    # raise Exception
                    break

def main(lines):
    # get numbers
    nums = lines[0]
    # load the boards
    boards = []
    currentBoardLines = []
    for _line in lines[1:]:
        line = _line.strip()
        if not line:
            if currentBoardLines:
                boards.append(Board(currentBoardLines))
            currentBoardLines = []
        else:
            currentBoardLines.append(line)
    boards.append(Board(currentBoardLines))
    for num in nums.split(','):
        for board in boards:
            if not board.won:
                board.pick(num)
        for i, board in enumerate(boards):
            if not board.won:
                print('checking board', i)
                board.check()


if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
