from sys import argv
from collections import defaultdict


def main(lines):
    generations = defaultdict(int)
    for timer in lines[0].split(','):
        generations[int(timer)] += 1
    print('Initial state:', generations)
    for i in range(256):
        def yieldItems():
            for timer, count in generations.items():
                if timer == 0:
                    yield 6, count
                    yield 8, count
                else:
                    yield timer - 1, count
        ng = defaultdict(int)
        for timer, count in yieldItems():
            ng[timer] += count
        generations = ng
        print(i + 1, generations)
    print(sum(generations.values()))


if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
