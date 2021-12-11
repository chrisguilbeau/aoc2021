from sys import argv

def main(lines):
    horizontal = 0
    aim = 0
    depth = 0
    for line in lines:
        direction, unitsText = line.split()
        units = int(unitsText) * (-1 if direction.startswith('u') else 1)
        if direction.startswith('f'):
            horizontal += units
            depth += units * aim
        else:
            aim += units
    print(horizontal * depth)

if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
