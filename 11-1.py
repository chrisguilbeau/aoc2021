from sys import argv


class Octo:
    def __init__(self, energyLevel, coord):
        self.energyLevel = energyLevel
        self.coord = coord
        self.neighbors = []
        self.flashed = False

    def addNeighbor(self, octo):
        self.neighbors.append(octo)

    def energize(self):
        if not self.flashed:
            self.energyLevel += 1

    def flash(self):
        if self.energyLevel > 9:
            print(self.coord, 'flashed', self.energyLevel)
            print([n.coord for n in self.neighbors])
            self.flashed = True
            self.energyLevel = 0
            for octo in self.neighbors:
                octo.energize()
            return True


def printField(field):
    cur = 0
    for (i, j), octo in field.items():
        if i > cur:
            print()
            cur = i
        print(octo.energyLevel, end='')
    print()
    print()


def main(lines):
    field = {}
    minI, minJ = (0, 0)
    for i, line in enumerate(lines):
        for j, energyLevel in enumerate(line.strip()):
            field[i, j] = Octo(int(energyLevel), (i, j))
    maxI, maxJ = (i, j)
    for (i, j), octo in field.items():
        neighbors = []
        if i > minI:
            neighbors.append(field[i - 1, j])
        if i < maxI:
            neighbors.append(field[i + 1, j])
        if j > minJ:
            neighbors.append(field[i, j - 1])
        if j < maxJ:
            neighbors.append(field[i, j + 1])
        if i > minI and j > minJ:
            neighbors.append(field[i - 1, j - 1])
        if i < maxI and j < maxJ:
            neighbors.append(field[i + 1, j + 1])
        if i > minI and j < maxJ:
            neighbors.append(field[i - 1, j + 1])
        if i < maxI and j > minJ:
            neighbors.append(field[i + 1, j - 1])
        octo.neighbors = neighbors
    printField(field)
    flashCount = 0
    for step in range(100):
        for octo in field.values():
            octo.flashed = False
            octo.energize()
        doFlash = True
        while doFlash:
            doFlash = False
            for octo in field.values():
                if octo.flash():
                    flashCount += 1
                    doFlash = True
            # printField(field)
        print('step', step + 1)
        printField(field)
    print(flashCount)


if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
