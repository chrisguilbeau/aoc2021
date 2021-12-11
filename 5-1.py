from sys import argv

def getEndPoints(line):
    parts = line.split()
    getPoint = lambda part: tuple(map(int,part.split(',')))
    return getPoint(parts[0]), getPoint(parts[-1])

def draw(grid):
    for i in range(10):
        for j in range(10):
            print(grid[(j, i)], end=' ')
        print()

def yieldPoints(p1, p2):
    cx = p1[0]
    cy = p1[1]
    while (cx, cy) != p2:
        print((cx, cy), '!=', p2)
        yield (cx, cy)
        if cx < p2[0]:
            cx += 1
        elif cx > p2[0]:
            cx -= 1
        if cy < p2[1]:
            cy += 1
        elif cy > p2[1]:
            cy -= 1
    yield p2

def main(lines):
    # set up grid
    grid = {}
    for i in range(1000):
        for j in range(1000):
            grid[(i,j)] = 0
    for line in lines:
        p1, p2 = sorted(getEndPoints(line))
        for coord in yieldPoints(p1, p2):
            grid[coord] += 1
        # if p1[0] == p2[0]:
        #     for i in range(p1[1], p2[1] + 1):
        #         grid[(p1[0], i)] += 1
        # if p1[1] == p2[1]:
        #     print(p1, p2)
        #     for i in range(p1[0], p2[0] + 1):
        #         grid[(i, p1[1])] += 1
    draw(grid)
    # print([i for i in grid.items() if i[1] > 1])
    print(sum(1 for _, i in grid.items() if i > 1))

if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
