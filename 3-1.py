from sys import argv

def main(lines):
    l = [0] * len(lines[0].strip())
    for line in lines:
        for i, bit in enumerate(line.strip()):
            print(i, bit, l)
            l[i] += 1 * (-1 if bit == '0' else 1)
    gamma = []
    epsilon = []
    for b in l:
        if b > 0:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)
    print(int(''.join(map(str, gamma)), 2) *
          int(''.join(map(str, epsilon)), 2))

if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
