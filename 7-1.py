from sys import argv
from collections import defaultdict


def getCost(depths, pos):
    result = 0
    for depth in depths:
        result += abs(pos - depth)
    return result

def main(lines):
    depths = list(map(int, lines[0].split(',')))
    print(depths)
    print(min(depths))
    print(max(depths))
    costs = []
    for i in range(min(depths), max(depths) + 1):
        costs.append((i, getCost(depths, i)))
    print(sorted(costs, key=lambda c: c[1])[0])


if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
