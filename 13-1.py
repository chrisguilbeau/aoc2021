from sys import argv


class Paper:
    def __init__(self, lines):
        maxX = 0
        maxY = 0
        points = {}
        for line in lines:
            x, y = map(int, map(str.strip, line.split(',')))
            points[(x, y)] = 0
            if x > maxX:
                maxX = x
            if y > maxY:
                maxY = y
        self.maxX = maxX
        self.maxY = maxY
        self.points = points

    def __str__(self):
        def yieldLines():
            dotCount = 0
            for y in range(self.maxY + 1):
                for x in range(self.maxX + 1):
                    if (x, y) in self.points:
                        yield '#'
                        dotCount += 1
                    else:
                        yield '.'
                yield '\n'
            yield f'{dotCount} dots'
            yield '\n'
        return ''.join(yieldLines())

    def foldY(self, f):
        newPoints = {}
        for x, y in self.points:
            if y > f:
                newY = y - ((y - f) * 2)
            else:
                newY = y
            newPoints[(x, newY)] = 0
        self.maxY = f
        self.points = newPoints

    def foldX(self, f):
        newPoints = {}
        for x, y in self.points:
            if x > f:
                newX = x - ((x - f) * 2)
            else:
                newX = x
            newPoints[(newX, y)] = 0
        self.maxX = f
        self.points = newPoints


def main(lines):
    pointLines = []
    foldLines = []
    curLines = pointLines
    for line in lines:
        if not line.strip():
            curLines = foldLines
            continue
        curLines.append(line)
    paper = Paper(pointLines)
    print(paper)
    for line in foldLines:
        axis, val = line.split()[-1].split('=')
        if axis == 'x':
            paper.foldX(int(val))
        else:
            paper.foldY(int(val))
        print(len(paper.points))
        print(paper)


if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
