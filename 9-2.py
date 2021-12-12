from sys import argv


class Heightmap:
    def __init__(self, lines):
        pointMap = {}
        self.minPoint = (0, 0)

        for i, line in enumerate(lines):
            for j, height in enumerate(line.strip()):
                point = (i, j)
                pointMap[point] = int(height)
        self.maxPoint = point
        self.pointMap = pointMap

    def yieldAdjacentPoints(self, point, ignore={}):
        minPoint = self.minPoint
        maxPoint = self.maxPoint
        i, j = point
        up = (i - 1, j)
        down = (i + 1, j)
        left = (i, j - 1)
        right = (i, j + 1)
        if i != minPoint[0] and up not in ignore:
            yield up
        if i != maxPoint[0] and down not in ignore:
            yield down
        if j != maxPoint[1] and right not in ignore:
            yield right
        if j != minPoint[1] and left not in ignore:
            yield left

    def yieldAdjacents(self, point):
        pointMap = self.pointMap
        for p in self.yieldAdjacentPoints(point):
            yield pointMap[p]

    def yieldLowPoints(self):
        for point, height in self.pointMap.items():
            if all(height < ad for ad in self.yieldAdjacents(point)):
                yield point

    def yieldLows(self):
        for lowPoint in self.yieldLowPoints():
            yield self.pointMap[lowPoint]

    def yieldBasin(self, lowPoint, ignore=None):
        print('b', end='')
        ignore = set() if ignore is None else ignore
        if lowPoint in ignore:
            return
        ignore.add(lowPoint)
        yield lowPoint
        for p in self.yieldAdjacentPoints(lowPoint, ignore=ignore):
            if self.pointMap[p] < 9:
                yield from self.yieldBasin(p, ignore)

    def yieldBasins(self):
        for lowPoint in self.yieldLowPoints():
            yield self.yieldBasin(lowPoint)


def main(lines):
    heightMap = Heightmap(lines)
    basins = []
    for b in heightMap.yieldBasins():
        sb = set(b)
        basins.append((len(sb), sb))
    big3 = [b for _, b in list(reversed(sorted(basins)))[:3]]
    print(big3)
    result = 1
    for b in big3:
        result = result * len(b)
    print(result)

if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
