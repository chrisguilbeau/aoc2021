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

    def yieldLows(self):
        minPoint = self.minPoint
        maxPoint = self.maxPoint
        pointMap = self.pointMap
        for point, height in self.pointMap.items():
            i, j = point
            if i == minPoint[0]:
                upLow = True
            else:
                upLow = height < pointMap[(i - 1, j)]
            if i == maxPoint[0]:
                downLow = True
            else:
                downLow = height < pointMap[(i + 1, j)]
            if j == maxPoint[1]:
                rightLow = True
            else:
                rightLow = height < pointMap[(i, j + 1)]
            if j == minPoint[1]:
                leftLow = True
            else:
                leftLow = height < pointMap[(i, j - 1)]
            if upLow and downLow and leftLow and rightLow:
                yield height


def main(lines):
    heightMap = Heightmap(lines)
    print(sum(h + 1 for h in heightMap.yieldLows()))


if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
