from sys import argv

def main(ints):
    print len([i for i in enumerate(ints)
                if i[0] > 0 and ints[i[0] - 1] < ints[i[0]]])

if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        ints = list(map(int, f.readlines()))
    main(ints)
